"""
Career explorer, recommendation ("guidance flow"), comparison, and
eligibility-checker routes. This is the core content engine of CareerVerse.
"""
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Query, status
from app.database import get_db
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.schemas.career import CareerGuidanceRequest, CareerCompareRequest
from app.auth.dependencies import get_current_user
from app.utils.recommendation_engine import find_best_career_match, get_related_careers, check_eligibility

router = APIRouter(prefix="/api/careers", tags=["Careers"])


def _serialize(career: dict) -> dict:
    career = dict(career)
    career["_id"] = str(career["_id"])
    return career


@router.get("")
async def list_careers(
    category: str | None = Query(default=None),
    stream: str | None = Query(default=None),
    search: str | None = Query(default=None),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    """Browse all careers, with optional filters - powers the Career Explorer page."""
    query: dict = {}
    if category:
        query["category"] = category
    if stream:
        query["streams"] = stream
    if search:
        query["$or"] = [
            {"title": {"$regex": search, "$options": "i"}},
            {"short_description": {"$regex": search, "$options": "i"}},
        ]

    careers = await db.careers.find(query).to_list(length=200)
    return [_serialize(c) for c in careers]


@router.get("/categories")
async def list_categories(db: AsyncIOMotorDatabase = Depends(get_db)):
    categories = await db.careers.distinct("category")
    return {"categories": sorted(categories)}


@router.get("/{slug}")
async def get_career_detail(slug: str, db: AsyncIOMotorDatabase = Depends(get_db)):
    career = await db.careers.find_one({"slug": slug})
    if not career:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Career not found")
    return _serialize(career)


@router.post("/guidance")
async def get_career_guidance(
    payload: CareerGuidanceRequest,
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    """
    The main career-guidance flow: takes the user's profile + dream career
    and returns a full personalized guidance report, matched against the
    careers database.
    """
    all_careers = await db.careers.find({}).to_list(length=500)
    matched = find_best_career_match(payload.dream_career, all_careers)

    if not matched:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"We couldn't find a close match for '{payload.dream_career}' yet. Try browsing the Career Explorer or rephrasing (e.g. 'Software Engineer', 'Doctor', 'Lawyer').",
        )

    eligibility_results = []
    for exam in matched.get("entrance_exams", []):
        verdict = check_eligibility(payload.age, payload.percentage, payload.education, exam)
        eligibility_results.append({"exam_name": exam["name"], **verdict})

    related = get_related_careers(matched, all_careers, payload.stream)

    # Log to career_history for the dashboard + admin analytics
    await db.career_history.insert_one({
        "user_id": current_user["_id"],
        "input": payload.model_dump(),
        "matched_career_slug": matched["slug"],
        "created_at": datetime.now(timezone.utc),
    })

    return {
        "career": _serialize(matched),
        "eligibility": eligibility_results,
        "related_careers": [_serialize(c) for c in related],
        "input_summary": payload.model_dump(),
    }


@router.post("/compare")
async def compare_careers(payload: CareerCompareRequest, db: AsyncIOMotorDatabase = Depends(get_db)):
    careers = await db.careers.find({"slug": {"$in": payload.career_slugs}}).to_list(length=10)
    if len(careers) < 2:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="At least 2 valid career slugs are required for comparison")
    return {"careers": [_serialize(c) for c in careers]}


@router.get("/history/me")
async def get_my_career_history(
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    history = await db.career_history.find({"user_id": current_user["_id"]}).sort("created_at", -1).to_list(length=50)
    for h in history:
        h["_id"] = str(h["_id"])
    return history
