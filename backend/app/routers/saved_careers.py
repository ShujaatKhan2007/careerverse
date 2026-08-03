"""Saved / bookmarked careers routes."""
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, status

from app.database import get_db
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.schemas.career import SaveCareerRequest
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/api/saved-careers", tags=["Saved Careers"])


@router.get("")
async def get_saved_careers(
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    saved = await db.saved_careers.find({"user_id": current_user["_id"]}).to_list(length=100)
    slugs = [s["career_slug"] for s in saved]
    careers = await db.careers.find({"slug": {"$in": slugs}}).to_list(length=100)
    careers_by_slug = {c["slug"]: c for c in careers}

    result = []
    for s in saved:
        career = careers_by_slug.get(s["career_slug"])
        if career:
            career = dict(career)
            career["_id"] = str(career["_id"])
            result.append({
                "saved_id": str(s["_id"]),
                "notes": s.get("notes"),
                "saved_at": s.get("saved_at"),
                "career": career,
            })
    return result


@router.post("", status_code=status.HTTP_201_CREATED)
async def save_career(
    payload: SaveCareerRequest,
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    career = await db.careers.find_one({"slug": payload.career_slug})
    if not career:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Career not found")

    existing = await db.saved_careers.find_one({"user_id": current_user["_id"], "career_slug": payload.career_slug})
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Career already saved")

    await db.saved_careers.insert_one({
        "user_id": current_user["_id"],
        "career_slug": payload.career_slug,
        "notes": payload.notes,
        "saved_at": datetime.now(timezone.utc),
    })
    return {"message": "Career saved successfully"}


@router.delete("/{career_slug}")
async def unsave_career(
    career_slug: str,
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    result = await db.saved_careers.delete_one({"user_id": current_user["_id"], "career_slug": career_slug})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Saved career not found")
    return {"message": "Career removed from saved list"}
