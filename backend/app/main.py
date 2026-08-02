"""
CareerVerse API - main FastAPI application entrypoint.

Run locally:
    uvicorn app.main:app --reload

Deploy on Render with start command:
    uvicorn app.main:app --host 0.0.0.0 --port $PORT
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.database import connect_to_mongo, close_mongo_connection
from app.routers import auth, users, careers, saved_careers, study_plans, chat, notifications, admin

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_to_mongo()
    yield
    await close_mongo_connection()


app = FastAPI(
    title="CareerVerse API",
    description="AI-powered career guidance platform - discover your career, build your future.",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(careers.router)
app.include_router(saved_careers.router)
app.include_router(study_plans.router)
app.include_router(chat.router)
app.include_router(notifications.router)
app.include_router(admin.router)


@app.get("/")
async def root():
    return {
        "name": "CareerVerse API",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}
