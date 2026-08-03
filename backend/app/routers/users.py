"""User profile routes."""
from bson import ObjectId
from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.database import get_db
from app.schemas.user import UserProfileUpdate, UserOut
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/api/users", tags=["Users"])


@router.put("/profile", response_model=UserOut)
async def update_profile(
    payload: UserProfileUpdate,
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    updates = {k: v for k, v in payload.model_dump().items() if v is not None}
    if updates:
        await db.users.update_one({"_id": ObjectId(current_user["_id"])}, {"$set": updates})

    updated_user = await db.users.find_one({"_id": ObjectId(current_user["_id"])})
    return UserOut(
        id=str(updated_user["_id"]),
        name=updated_user["name"],
        email=updated_user["email"],
        role=updated_user.get("role", "user"),
        age=updated_user.get("age"),
        education=updated_user.get("education"),
        stream=updated_user.get("stream"),
        percentage=updated_user.get("percentage"),
        dream_career=updated_user.get("dream_career"),
        bio=updated_user.get("bio"),
        location=updated_user.get("location"),
        created_at=updated_user.get("created_at"),
    )


@router.get("/dashboard-summary")
async def dashboard_summary(
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    """Aggregated counts for the dashboard's progress overview widgets."""
    user_id = current_user["_id"]
    saved_count = await db.saved_careers.count_documents({"user_id": user_id})
    plans_count = await db.study_plans.count_documents({"user_id": user_id})
    history_count = await db.career_history.count_documents({"user_id": user_id})

    plans = await db.study_plans.find({"user_id": user_id}).to_list(length=100)
    total_tasks = sum(len(p.get("tasks", [])) for p in plans)
    completed_tasks = sum(sum(1 for t in p.get("task_status", []) if t) for p in plans)
    progress_pct = round((completed_tasks / total_tasks) * 100, 1) if total_tasks else 0

    recent_activity = await db.career_history.find({"user_id": user_id}).sort("created_at", -1).to_list(length=5)
    for r in recent_activity:
        r["_id"] = str(r["_id"])

    return {
        "saved_careers_count": saved_count,
        "study_plans_count": plans_count,
        "careers_explored_count": history_count,
        "overall_progress_pct": progress_pct,
        "recent_activity": recent_activity,
    }
