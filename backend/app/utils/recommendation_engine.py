"""
Lightweight recommendation engine that matches a user's dream career input
(free text) against the careers collection, and suggests alternative
careers based on stream/education/interest overlap.

Kept dependency-free (no external ML libs) so it runs fast on Render's
free tier; can be swapped for an embeddings-based matcher later without
touching the router layer.
"""
import re
from difflib import SequenceMatcher

ALIASES = {
    "software engineer": ["developer", "programmer", "swe", "coder", "software developer", "web developer", "app developer"],
    "doctor": ["mbbs", "physician", "medical doctor", "surgeon"],
    "chartered accountant": ["ca", "accountant", "auditor"],
    "civil services ias": ["ias", "ips", "civil services", "collector", "bureaucrat", "upsc"],
    "data scientist": ["data science", "machine learning engineer", "ml engineer", "ai engineer", "data analyst"],
    "lawyer": ["advocate", "attorney", "legal", "law"],
    "mechanical engineer": ["mechanical engineering"],
    "architect": ["architecture"],
    "commercial pilot": ["pilot", "aviator", "airline pilot"],
    "fashion designer": ["fashion design", "fashion designing"],
    "psychologist": ["psychology", "therapist", "counselor", "counsellor"],
    "teacher professor": ["teacher", "professor", "educator", "lecturer"],
    "journalist": ["journalism", "reporter", "news anchor", "media"],
    "product manager": ["product management", "pm"],
    "army officer": [
        "army", "defence", "military officer", "soldier officer", "nda", "cds",
        "afcat", "navy", "air force", "navy officer", "air force officer",
        "defence officer", "indian army", "indian navy", "indian air force", "pilot officer",
    ],
    "pharmacist": ["pharmacy", "pharmaceutical"],
    "state civil services": ["mpsc", "state psc", "deputy collector", "tehsildar", "state pcs", "uppsc", "bpsc"],
    "ssc government officer": [
        "ssc", "ssc cgl", "ssc chsl", "staff selection commission", "government job",
        "sarkari naukri", "govt job", "income tax inspector", "clerk",
    ],
    "cybersecurity analyst": ["cybersecurity", "cyber security", "ethical hacker", "security analyst", "infosec", "penetration tester"],
    "cloud devops engineer": ["devops", "cloud engineer", "cloud computing", "sre", "site reliability engineer"],
    "dentist": ["bds", "dental surgeon", "dental doctor"],
    "nurse": ["nursing", "staff nurse", "bsc nursing", "gnm"],
    "physiotherapist": ["physiotherapy", "bpt", "physical therapist"],
    "civil engineer": ["civil engineering"],
    "electrical electronics engineer": ["electrical engineer", "electronics engineer", "eee", "ece"],
    "company secretary": ["cs", "company secretary", "corporate secretary"],
    "bank po": ["bank job", "banking", "ibps", "sbi po", "probationary officer", "bank clerk"],
    "judge": ["judiciary", "judicial services", "magistrate", "civil judge"],
    "graphic uiux designer": ["graphic designer", "ui designer", "ux designer", "ui ux", "product designer", "visual designer"],
    "digital marketing specialist": ["digital marketing", "seo", "social media marketing", "content marketing", "marketing"],
    "hr manager": ["human resources", "hr", "talent acquisition", "recruiter"],
    "aircraft maintenance engineer": ["ame", "aircraft engineer", "aviation maintenance"],
    "special education teacher": ["special educator", "special education", "inclusive education teacher"],
}


def _normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9\s]", "", text.lower()).strip()


def _similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def find_best_career_match(dream_career_input: str, careers: list[dict]) -> dict | None:
    """
    Matches free-text dream career input to the closest career in the DB.
    Strategy: exact/alias match first, then fuzzy string similarity fallback.
    """
    normalized_input = _normalize(dream_career_input)
    if not normalized_input:
        return None

    # 1. Direct slug/title match
    for career in careers:
        if normalized_input == _normalize(career["title"]) or normalized_input == career["slug"].replace("-", " "):
            return career

    # 2a. Exact alias match (checked across ALL careers before any fuzzy/substring
    # matching below) - this must run first so an exact alias like "afcat" can't
    # be shadowed by an unrelated career whose short alias (e.g. "ca") happens
    # to appear as a substring of the input.
    for career in careers:
        key = career["slug"].replace("-", " ")
        aliases = ALIASES.get(key, [])
        if normalized_input in aliases:
            return career

    # 2b. Substring alias match - only reached if no exact alias matched above
    for career in careers:
        key = career["slug"].replace("-", " ")
        aliases = ALIASES.get(key, [])
        if any(normalized_input in a or a in normalized_input for a in aliases):
            return career

    # 3. Substring match against title
    for career in careers:
        title_norm = _normalize(career["title"])
        if normalized_input in title_norm or title_norm in normalized_input:
            return career

    # 4. Word-overlap match - handles full sentences/questions with an embedded
    # career name, e.g. "What is the salary of a doctor?" -> Doctor (MBBS)
    input_words = set(normalized_input.split())
    stop_words = {"of", "and", "the", "a", "an", "in", "for", "to"}
    best_overlap, best_overlap_score = None, 0.0
    for career in careers:
        title_words = set(_normalize(career["title"]).split()) - stop_words
        if not title_words:
            continue
        overlap = title_words & input_words
        if overlap:
            score = len(overlap) / len(title_words)
            if score > best_overlap_score:
                best_overlap, best_overlap_score = career, score
    if best_overlap and best_overlap_score >= 0.4:
        return best_overlap

    # 5. Fuzzy match fallback - best similarity score above threshold
    best_match, best_score = None, 0.0
    for career in careers:
        score = _similarity(normalized_input, _normalize(career["title"]))
        if score > best_score:
            best_match, best_score = career, score

    return best_match if best_score >= 0.45 else None


def get_related_careers(matched_career: dict, all_careers: list[dict], user_stream: str, limit: int = 3) -> list[dict]:
    """
    Suggests related/alternative careers based on category and stream overlap,
    useful for the 'You might also like' section and career comparison tool.
    """
    candidates = [
        c for c in all_careers
        if c["slug"] != matched_career["slug"]
        and (c["category"] == matched_career["category"] or user_stream in c.get("streams", []))
    ]
    # Prioritize same category first, then same stream
    candidates.sort(key=lambda c: (c["category"] != matched_career["category"]))
    return candidates[:limit]


def check_eligibility(user_age: int, user_percentage: float, user_education: str, exam: dict) -> dict:
    """
    Basic rule-based eligibility checker against an exam's stated requirements.
    Returns a structured verdict the frontend can render directly.
    """
    notes = []
    eligible = True

    age_limit_text = exam.get("age_limit", "")
    # Very lightweight numeric age-range extraction (best-effort, not a legal determination)
    age_numbers = re.findall(r"\d{2}", age_limit_text)
    if len(age_numbers) >= 2:
        low, high = int(age_numbers[0]), int(age_numbers[1])
        if not (low <= user_age <= high):
            eligible = False
            notes.append(f"Your age ({user_age}) may fall outside the typical range ({low}-{high}) stated for this exam.")

    if user_percentage < 50:
        notes.append("Your percentage is below the commonly required 50% minimum for many programs - check the specific exam's cutoff, as reserved categories often have relaxations.")

    if not notes:
        notes.append("Based on the details provided, you appear to meet the general eligibility criteria. Always verify against the latest official notification.")

    return {"eligible": eligible, "notes": notes}
