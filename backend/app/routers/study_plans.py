"""Study planner + progress tracker routes."""
from datetime import datetime, timezone
from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.database import get_db
from app.schemas.career import StudyPlanCreate, StudyPlanTaskUpdate
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/api/study-plans", tags=["Study Plans"])


def _serialize(plan: dict) -> dict:
    plan = dict(plan)
    plan["_id"] = str(plan["_id"])
    tasks = plan.get("tasks", [])
    status_list = plan.get("task_status", [False] * len(tasks))
    plan["task_status"] = status_list
    plan["progress_pct"] = round((sum(status_list) / len(tasks)) * 100, 1) if tasks else 0
    return plan


@router.get("")
async def list_study_plans(
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    plans = await db.study_plans.find({"user_id": current_user["_id"]}).sort("created_at", -1).to_list(length=100)
    return [_serialize(p) for p in plans]


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_study_plan(
    payload: StudyPlanCreate,
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    career = await db.careers.find_one({"slug": payload.career_slug})
    if not career:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Career not found")

    doc = {
        "user_id": current_user["_id"],
        "career_slug": payload.career_slug,
        "title": payload.title,
        "exam_name": payload.exam_name,
        "target_date": payload.target_date,
        "tasks": payload.tasks,
        "task_status": [False] * len(payload.tasks),
        "created_at": datetime.now(timezone.utc),
    }
    result = await db.study_plans.insert_one(doc)
    doc["_id"] = result.inserted_id
    return _serialize(doc)


@router.patch("/{plan_id}/task")
async def update_task_status(
    plan_id: str,
    payload: StudyPlanTaskUpdate,
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    plan = await db.study_plans.find_one({"_id": ObjectId(plan_id), "user_id": current_user["_id"]})
    if not plan:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Study plan not found")

    task_status = plan.get("task_status", [False] * len(plan.get("tasks", [])))
    if payload.task_index >= len(task_status):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid task index")

    task_status[payload.task_index] = payload.completed
    await db.study_plans.update_one({"_id": ObjectId(plan_id)}, {"$set": {"task_status": task_status}})

    updated = await db.study_plans.find_one({"_id": ObjectId(plan_id)})
    return _serialize(updated)


@router.delete("/{plan_id}")
async def delete_study_plan(
    plan_id: str,
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    result = await db.study_plans.delete_one({"_id": ObjectId(plan_id), "user_id": current_user["_id"]})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Study plan not found")
    return {"message": "Study plan deleted"}
