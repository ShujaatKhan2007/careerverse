"""Notifications routes - exam alerts, deadline reminders, official announcements."""
from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.database import get_db
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/api/notifications", tags=["Notifications"])


@router.get("")
async def get_notifications(
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    # Notifications targeted at this user, plus global ones (user_id: null)
    notifications = await db.notifications.find(
        {"$or": [{"user_id": current_user["_id"]}, {"user_id": None}]}
    ).sort("created_at", -1).to_list(length=50)
    for n in notifications:
        n["_id"] = str(n["_id"])
    return notifications


@router.patch("/{notification_id}/read")
async def mark_as_read(
    notification_id: str,
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    result = await db.notifications.update_one(
        {"_id": ObjectId(notification_id), "$or": [{"user_id": current_user["_id"]}, {"user_id": None}]},
        {"$addToSet": {"read_by": current_user["_id"]}},
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notification not found")
    return {"message": "Marked as read"}
