"""AI Career Assistant chat routes."""
import json
import uuid
from datetime import datetime, timezone
from fastapi import APIRouter, Depends

from app.database import get_db
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.schemas.career import ChatMessageRequest
from app.auth.dependencies import get_current_user
from app.utils.chat_engine import generate_rule_based_response, generate_llm_response

router = APIRouter(prefix="/api/chat", tags=["AI Assistant"])

SUGGESTED_QUESTIONS = [
    "How do I become a doctor?",
    "What is the salary of a software engineer?",
    "Best books to prepare for CA Foundation?",
    "Compare data scientist vs software engineer",
    "What are the eligibility criteria for NEET?",
]


@router.get("/suggestions")
async def get_suggested_questions():
    return {"suggestions": SUGGESTED_QUESTIONS}


@router.post("/message")
async def send_chat_message(
    payload: ChatMessageRequest,
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    session_id = payload.session_id or str(uuid.uuid4())

    all_careers = await db.careers.find({}).to_list(length=500)

    # Pull recent history for this session to give the LLM (if enabled) conversation context
    history_doc = await db.chat_history.find_one({"user_id": current_user["_id"], "session_id": session_id})
    prior_messages = history_doc.get("messages", []) if history_doc else []

    llm_context = "\n".join(
        f"{c['title']}: {c['short_description']}" for c in all_careers
    )
    llm_reply = await generate_llm_response(
        payload.message,
        [{"role": m["role"], "content": m["content"]} for m in prior_messages[-10:]],
        llm_context,
    )

    reply = llm_reply or generate_rule_based_response(payload.message, all_careers, current_user.get("name", "there"))

    new_messages = prior_messages + [
        {"role": "user", "content": payload.message, "at": datetime.now(timezone.utc).isoformat()},
        {"role": "assistant", "content": reply, "at": datetime.now(timezone.utc).isoformat()},
    ]

    await db.chat_history.update_one(
        {"user_id": current_user["_id"], "session_id": session_id},
        {"$set": {"messages": new_messages, "updated_at": datetime.now(timezone.utc)},
         "$setOnInsert": {"user_id": current_user["_id"], "session_id": session_id, "created_at": datetime.now(timezone.utc)}},
        upsert=True,
    )

    return {"session_id": session_id, "reply": reply}


@router.get("/history/{session_id}")
async def get_chat_history(
    session_id: str,
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    history_doc = await db.chat_history.find_one({"user_id": current_user["_id"], "session_id": session_id})
    if not history_doc:
        return {"session_id": session_id, "messages": []}
    return {"session_id": session_id, "messages": history_doc.get("messages", [])}


@router.get("/sessions")
async def list_chat_sessions(
    current_user: dict = Depends(get_current_user),
    db: AsyncIOMotorDatabase = Depends(get_db),
):
    sessions = await db.chat_history.find(
        {"user_id": current_user["_id"]}, {"session_id": 1, "updated_at": 1, "messages": {"$slice": -1}}
    ).sort("updated_at", -1).to_list(length=30)
    for s in sessions:
        s["_id"] = str(s["_id"])
    return sessions
