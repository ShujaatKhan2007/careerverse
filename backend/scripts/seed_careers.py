"""
One-off script to seed/refresh the `careers` collection in MongoDB from
app/data/careers_data.py. Safe to re-run - it upserts by slug so existing
saved_careers/study_plans references stay valid.

Usage (from backend/ directory):
    python -m scripts.seed_careers
"""
import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from motor.motor_asyncio import AsyncIOMotorClient
from app.config import get_settings
from app.data.careers_data import CAREERS


async def seed():
    settings = get_settings()
    client = AsyncIOMotorClient(settings.mongo_uri)
    db = client[settings.mongo_db_name]

    for career in CAREERS:
        await db.careers.update_one(
            {"slug": career["slug"]},
            {"$set": career},
            upsert=True,
        )
        print(f"Upserted: {career['title']}")

    await db.careers.create_index("slug", unique=True)
    print(f"\nSeed complete. {len(CAREERS)} careers upserted.")
    client.close()


if __name__ == "__main__":
    asyncio.run(seed())
