"""
Creates (or promotes) the admin user defined by ADMIN_EMAIL / ADMIN_PASSWORD
in the environment. Safe to re-run.

Usage (from backend/ directory):
    python -m scripts.create_admin
"""
import asyncio
import sys
import os
from datetime import datetime, timezone

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from motor.motor_asyncio import AsyncIOMotorClient
from app.config import get_settings
from app.auth.password import hash_password


async def create_admin():
    settings = get_settings()
    client = AsyncIOMotorClient(settings.mongo_uri)
    db = client[settings.mongo_db_name]

    existing = await db.users.find_one({"email": settings.admin_email})
    if existing:
        await db.users.update_one({"email": settings.admin_email}, {"$set": {"role": "admin"}})
        print(f"Existing user {settings.admin_email} promoted to admin.")
    else:
        await db.users.insert_one({
            "name": "CareerVerse Admin",
            "email": settings.admin_email,
            "password_hash": hash_password(settings.admin_password),
            "role": "admin",
            "created_at": datetime.now(timezone.utc),
        })
        print(f"Admin user created: {settings.admin_email}")

    client.close()


if __name__ == "__main__":
    asyncio.run(create_admin())
