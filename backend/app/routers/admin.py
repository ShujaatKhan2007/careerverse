"""
Admin dashboard routes: platform analytics, user management, and
career/exam content management (CRUD on the careers collection).
Protected by get_current_admin - requires role == "admin".
"""
from datetime import datetime, timezone
from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.database import get_db
from app.auth.dependencies import get_current_admin

router = APIRouter(prefix="/api/admin", tags=["Admin"])


@router.get("/stats")
async def get_platform_stats(
    _admin: dict = Depends(get_current_admin),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    total_users = await db.users.count_documents({})
    total_careers = await db.careers.count_documents({})
    total_guidance_requests = await db.career_history.count_documents({})
    total_study_plans = await db.study_plans.count_documents({})
    total_chat_sessions = await db.chat_history.count_documents({})

    pipeline = [
        {"$group": {"_id": "$matched_career_slug", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 5},
    ]
    top_careers = await db.career_history.aggregate(pipeline).to_list(length=5)

    return {
        "total_users": total_users,
        "total_careers": total_careers,
        "total_guidance_requests": total_guidance_requests,
        "total_study_plans": total_study_plans,
        "total_chat_sessions": total_chat_sessions,
        "top_requested_careers": top_careers,
    }


@router.get("/users")
async def list_all_users(
    _admin: dict = Depends(get_current_admin),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    users = await db.users.find({}, {"password_hash": 0}).sort("created_at", -1).to_list(length=500)
    for u in users:
        u["_id"] = str(u["_id"])
    return users


@router.delete("/users/{user_id}")
async def delete_user(
    user_id: str,
    _admin: dict = Depends(get_current_admin),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    result = await db.users.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {"message": "User deleted"}


@router.post("/careers", status_code=status.HTTP_201_CREATED)
async def create_career(
    career: dict,
    _admin: dict = Depends(get_current_admin),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    """Add a new career to the platform - no code changes needed elsewhere."""
    if not career.get("slug") or not career.get("title"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="'slug' and 'title' are required")

    existing = await db.careers.find_one({"slug": career["slug"]})
    if existing:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="A career with this slug already exists")

    await db.careers.insert_one(career)
    return {"message": "Career created", "slug": career["slug"]}


@router.put("/careers/{slug}")
async def update_career(
    slug: str,
    updates: dict,
    _admin: dict = Depends(get_current_admin),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    result = await db.careers.update_one({"slug": slug}, {"$set": updates})
    if result.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Career not found")
    return {"message": "Career updated"}


@router.delete("/careers/{slug}")
async def delete_career(
    slug: str,
    _admin: dict = Depends(get_current_admin),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    result = await db.careers.delete_one({"slug": slug})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Career not found")
    return {"message": "Career deleted"}


@router.post("/notifications", status_code=status.HTTP_201_CREATED)
async def create_notification(
    notification: dict,
    _admin: dict = Depends(get_current_admin),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    """Broadcast a notification. Omit user_id (or set null) for a global/platform-wide notice."""
    notification.setdefault("user_id", None)
    notification.setdefault("read_by", [])
    notification["created_at"] = datetime.now(timezone.utc)
    result = await db.notifications.insert_one(notification)
    return {"message": "Notification created", "id": str(result.inserted_id)}
