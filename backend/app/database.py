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


async def close_mongo_connection():
    if mongo.client:
        mongo.client.close()


def get_db() -> AsyncIOMotorDatabase:
    """Dependency-injectable accessor for the active database."""
    return mongo.db
