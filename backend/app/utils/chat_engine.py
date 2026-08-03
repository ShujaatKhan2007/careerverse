"""
AI Career Assistant response engine.

Ships as a fast, dependency-free retrieval/rule-based assistant that answers
from the careers dataset (no API cost, works out of the box). If GEMINI_API_KEY
or ANTHROPIC_API_KEY is set in the environment, `generate_llm_response` calls
that provider instead for genuinely open-ended conversation, falling back to
the rule-based engine if neither key is set or the call fails. If both are
set, Gemini is tried first.
"""
import os
import re
from app.utils.recommendation_engine import find_best_career_match, _normalize

GREETINGS = ["hi", "hello", "hey", "hii", "hlo"]


def generate_rule_based_response(
    message: str,
    careers: list[dict],
    user_name: str = "there",
    last_career_slug: str | None = None,
) -> tuple[str, str | None]:
    """
    Returns (reply_text, matched_career_slug_or_None).

    The caller should persist matched_career_slug and pass it back in as
    last_career_slug on the next turn - this lets vague follow-ups like
    "how to study" or "what about the salary" inherit the career being
    discussed, instead of failing to match on their own.
    """
    normalized = _normalize(message)

    if any(normalized == g or normalized.startswith(g + " ") for g in GREETINGS):
        return (
            f"Hi {user_name}! I'm your CareerVerse AI assistant. Ask me about any career, its entrance exams, eligibility, salary, or preparation strategy - for example, 'What is the salary of a data scientist?' or 'How do I become a doctor?'",
            None,
        )

    match = find_best_career_match(message, careers)

    # Vague follow-up with no career mentioned - inherit context from the
    # last career discussed in this session, if any.
    if not match and last_career_slug:
        match = next((c for c in careers if c["slug"] == last_career_slug), None)

    # Salary queries
    if "salary" in normalized or "pay" in normalized or "package" in normalized:
        if match:
            s = match["salary_range"]
            return (
                f"For a **{match['title']}**, typical salaries in India range from {s['entry']} at entry level, "
                f"growing to {s['mid']} mid-career, and {s['senior']} at senior levels. Growth path: {match['career_growth']}",
                match["slug"],
            )

    # Exam / eligibility queries
    if any(k in normalized for k in ["exam", "eligib", "entrance", "how do i become", "how to become"]):
        if match and match.get("entrance_exams"):
            exam = match["entrance_exams"][0]
            return (
                f"To become a **{match['title']}**, the key entrance exam is **{exam['name']}** "
                f"(conducted by {exam['conducting_body']}). Eligibility: {exam['eligibility']}. "
                f"Age limit: {exam['age_limit']}. Attempts allowed: {exam['attempts']}.",
                match["slug"],
            )

    # Books / preparation / study queries
    if any(k in normalized for k in ["book", "prepare", "preparation", "study material", "how to study", "study tips", "study plan"]):
        if match:
            books = ", ".join(match["best_books"][:3])
            strategy = match["preparation_strategy"][0] if match.get("preparation_strategy") else None
            reply = f"For **{match['title']}**, recommended books include: {books}."
            if strategy:
                reply += f" A good first step: {strategy}"
            reply += " Check the career's detail page for the full step-by-step preparation strategy."
            return (reply, match["slug"])

    # College queries
    if any(k in normalized for k in ["college", "university", "institute"]):
        if match:
            colleges = ", ".join(match["top_colleges"][:4])
            return (f"Some of the top colleges/institutes for **{match['title']}** are: {colleges}.", match["slug"])

    # Generic career match fallback
    if match:
        return (
            f"**{match['title']}**: {match['overview']} \n\nWould you like details on entrance exams, "
            f"required qualifications, salary range, or preparation strategy?",
            match["slug"],
        )

    return (
        "I couldn't find a specific match for that in my career database yet. "
        "Try asking about a specific career (e.g. 'Tell me about software engineering'), "
        "or use the Career Explorer to browse all available paths.",
        None,
    )


def _build_system_prompt(careers_context: str) -> str:
    return (
        "You are the CareerVerse AI Career Assistant. Help students with career guidance, "
        "exam eligibility, preparation strategy, and study resources. Be concise, encouraging, "
        "and specific. Use this career database context when relevant:\n\n" + careers_context
    )


async def _generate_gemini_response(message: str, conversation_history: list[dict], careers_context: str) -> str | None:
    """
    Calls the Gemini API if GEMINI_API_KEY is configured. Returns None if not
    configured (or the request fails) so the caller can fall back.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return None

    import httpx

    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    system_prompt = _build_system_prompt(careers_context)

    # Gemini's "contents" format uses role "model" instead of "assistant"
    contents = [
        {"role": "model" if m["role"] == "assistant" else "user", "parts": [{"text": m["content"]}]}
        for m in conversation_history
    ]
    contents.append({"role": "user", "parts": [{"text": message}]})

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(
                url,
                headers={"x-goog-api-key": api_key, "Content-Type": "application/json"},
                json={
                    "contents": contents,
                    "systemInstruction": {"parts": [{"text": system_prompt}]},
                    "generationConfig": {"maxOutputTokens": 500},
                },
            )
            resp.raise_for_status()
            data = resp.json()
            candidates = data.get("candidates", [])
            if not candidates:
                return None
            parts = candidates[0].get("content", {}).get("parts", [])
            return "".join(p.get("text", "") for p in parts) or None
    except Exception:
        # Fail closed - let the caller fall back to the rule-based engine
        # rather than surfacing a raw API error to the user.
        return None


async def _generate_anthropic_response(message: str, conversation_history: list[dict], careers_context: str) -> str | None:
    """
    Calls the Anthropic API if ANTHROPIC_API_KEY is configured. Returns None
    if not configured (or the request fails) so the caller can fall back.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return None

    import httpx

    system_prompt = _build_system_prompt(careers_context)
    messages = conversation_history + [{"role": "user", "content": message}]

    try:
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(
                "https://api.anthropic.com/v1/messages",
                headers={
                    "x-api-key": api_key,
                    "anthropic-version": "2023-06-01",
                    "content-type": "application/json",
                },
                json={
                    "model": "claude-sonnet-4-6",
                    "max_tokens": 500,
                    "system": system_prompt,
                    "messages": messages,
                },
            )
            resp.raise_for_status()
            data = resp.json()
            return "".join(block.get("text", "") for block in data.get("content", []) if block.get("type") == "text") or None
    except Exception:
        return None


async def generate_llm_response(message: str, conversation_history: list[dict], careers_context: str) -> str | None:
    """
    Tries Gemini first (if GEMINI_API_KEY is set), then Anthropic (if
    ANTHROPIC_API_KEY is set), then returns None so the caller falls back to
    the free rule-based engine. Neither key is required for the app to work.
    """
    result = await _generate_gemini_response(message, conversation_history, careers_context)
    if result:
        return result

    result = await _generate_anthropic_response(message, conversation_history, careers_context)
    if result:
        return result

    return None


async def test_gemini_connection() -> dict:
    """
    Diagnostic check for the /api/chat/provider-status endpoint. Makes a
    minimal real API call and reports exactly what happened - configured or
    not, working or not, and the specific error if it failed. Unlike the
    main chat flow, this does NOT fail silently.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return {"configured": False, "working": False, "error": None}

    import httpx

    model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

    try:
        async with httpx.AsyncClient(timeout=15) as client:
            resp = await client.post(
                url,
                headers={"x-goog-api-key": api_key, "Content-Type": "application/json"},
                json={"contents": [{"role": "user", "parts": [{"text": "Say 'test successful' and nothing else."}]}]},
            )
        if resp.status_code == 200:
            data = resp.json()
            candidates = data.get("candidates", [])
            text = "".join(p.get("text", "") for p in candidates[0].get("content", {}).get("parts", [])) if candidates else None
            return {"configured": True, "working": bool(text), "error": None, "sample_reply": text}
        else:
            return {"configured": True, "working": False, "error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"configured": True, "working": False, "error": f"{type(e).__name__}: {str(e)[:300]}"}


async def test_anthropic_connection() -> dict:
    """Diagnostic check mirroring test_gemini_connection() for Anthropic."""
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return {"configured": False, "working": False, "error": None}

    import httpx

    try:
        async with httpx.AsyncClient(timeout=15) as client:
            resp = await client.post(
                "https://api.anthropic.com/v1/messages",
                headers={"x-api-key": api_key, "anthropic-version": "2023-06-01", "content-type": "application/json"},
                json={
                    "model": "claude-sonnet-4-6",
                    "max_tokens": 20,
                    "messages": [{"role": "user", "content": "Say 'test successful' and nothing else."}],
                },
            )
        if resp.status_code == 200:
            data = resp.json()
            text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
            return {"configured": True, "working": bool(text), "error": None, "sample_reply": text}
        else:
            return {"configured": True, "working": False, "error": f"HTTP {resp.status_code}: {resp.text[:300]}"}
    except Exception as e:
        return {"configured": True, "working": False, "error": f"{type(e).__name__}: {str(e)[:300]}"}
        return result

    result = await _generate_anthropic_response(message, conversation_history, careers_context)
    if result:
        return result

    return None
