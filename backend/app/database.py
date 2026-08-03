"""
MongoDB (Motor async) connection manager.
Exposes a single Database instance shared across the app, plus
convenience accessors for each collection so the rest of the codebase
never hardcodes collection name strings.
"""
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.config import get_settings

settings = get_settings()


class MongoManager:
    client: AsyncIOMotorClient | None = None
    db: AsyncIOMotorDatabase | None = None


mongo = MongoManager()


async def connect_to_mongo():
    mongo.client = AsyncIOMotorClient(settings.mongo_uri)
    mongo.db = mongo.client[settings.mongo_db_name]
    # Helpful indexes - created idempotently on startup
    await mongo.db.users.create_index("email", unique=True)
    await mongo.db.careers.create_index("slug", unique=True)
    await mongo.db.saved_careers.create_index([("user_id", 1), ("career_slug", 1)], unique=True)
    await mongo.db.career_history.create_index("user_id")
    await mongo.db.chat_history.create_index("user_id")
    await mongo.db.study_plans.create_index("user_id")
    await mongo.db.notifications.create_index("user_id")
    await _seed_if_needed()


async def _seed_if_needed():
    """
    Runs automatically on every startup - no manual script or Shell access
    required (useful on hosts like Render's free tier where Shell is a paid
    feature). Upserts every career by slug (safe/idempotent, so this always
    keeps the database in sync with the latest app/data/careers_data.py),
    and creates the admin account from settings if it doesn't exist yet.
    """
    from datetime import datetime, timezone
    from app.data.careers_data import CAREERS
    from app.auth.password import hash_password

    for career in CAREERS:
        await mongo.db.careers.update_one({"slug": career["slug"]}, {"$set": career}, upsert=True)

    admin = await mongo.db.users.find_one({"email": settings.admin_email})
    if not admin:
        await mongo.db.users.insert_one({
            "name": "CareerVerse Admin",
            "email": settings.admin_email,
            "password_hash": hash_password(settings.admin_password),
            "role": "admin",
            "created_at": datetime.now(timezone.utc),
        })


async def close_mongo_connection():
    if mongo.client:
        mongo.client.close()


def get_db() -> AsyncIOMotorDatabase:
    """Dependency-injectable accessor for the active database."""
    return mongo.db
