"""
AI Career Assistant response engine.

Ships as a fast, dependency-free retrieval/rule-based assistant that answers
from the careers dataset (no API cost, works out of the box). If an
ANTHROPIC_API_KEY is set in the environment, `generate_llm_response` is used
instead for genuinely open-ended conversation - swap the flag in
routers/chat.py once you've added a key.
"""
import os
import re
from app.utils.recommendation_engine import find_best_career_match, _normalize

GREETINGS = ["hi", "hello", "hey", "hii", "hlo"]


def generate_rule_based_response(message: str, careers: list[dict], user_name: str = "there") -> str:
    normalized = _normalize(message)

    if any(normalized == g or normalized.startswith(g + " ") for g in GREETINGS):
        return f"Hi {user_name}! I'm your CareerVerse AI assistant. Ask me about any career, its entrance exams, eligibility, salary, or preparation strategy - for example, 'What is the salary of a data scientist?' or 'How do I become a doctor?'"

    # Salary queries
    if "salary" in normalized or "pay" in normalized or "package" in normalized:
        match = find_best_career_match(message, careers)
        if match:
            s = match["salary_range"]
            return (f"For a **{match['title']}**, typical salaries in India range from {s['entry']} at entry level, "
                    f"growing to {s['mid']} mid-career, and {s['senior']} at senior levels. Growth path: {match['career_growth']}")

    # Exam / eligibility queries
    if any(k in normalized for k in ["exam", "eligib", "entrance", "how do i become", "how to become"]):
        match = find_best_career_match(message, careers)
        if match and match.get("entrance_exams"):
            exam = match["entrance_exams"][0]
            return (f"To become a **{match['title']}**, the key entrance exam is **{exam['name']}** "
                    f"(conducted by {exam['conducting_body']}). Eligibility: {exam['eligibility']}. "
                    f"Age limit: {exam['age_limit']}. Attempts allowed: {exam['attempts']}.")

    # Books / preparation queries
    if any(k in normalized for k in ["book", "prepare", "preparation", "study material"]):
        match = find_best_career_match(message, careers)
        if match:
            books = ", ".join(match["best_books"][:3])
            return f"For **{match['title']}**, recommended books include: {books}. I'd also suggest checking the full preparation strategy on the career's detail page for a step-by-step plan."

    # College queries
    if any(k in normalized for k in ["college", "university", "institute"]):
        match = find_best_career_match(message, careers)
        if match:
            colleges = ", ".join(match["top_colleges"][:4])
            return f"Some of the top colleges/institutes for **{match['title']}** are: {colleges}."

    # Generic career match fallback
    match = find_best_career_match(message, careers)
    if match:
        return (f"**{match['title']}**: {match['overview']} \n\nWould you like details on entrance exams, "
                f"required qualifications, salary range, or preparation strategy?")

    return ("I couldn't find a specific match for that in my career database yet. "
            "Try asking about a specific career (e.g. 'Tell me about software engineering'), "
            "or use the Career Explorer to browse all available paths.")


async def generate_llm_response(message: str, conversation_history: list[dict], careers_context: str) -> str | None:
    """
    Optional: calls the Anthropic API for open-ended conversation if
    ANTHROPIC_API_KEY is configured. Returns None if not configured so the
    caller can fall back to the rule-based engine.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        return None

    import httpx

    system_prompt = (
        "You are the CareerVerse AI Career Assistant. Help students with career guidance, "
        "exam eligibility, preparation strategy, and study resources. Be concise, encouraging, "
        "and specific. Use this career database context when relevant:\n\n" + careers_context
    )
    messages = conversation_history + [{"role": "user", "content": message}]

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
        return "".join(block.get("text", "") for block in data.get("content", []) if block.get("type") == "text")
