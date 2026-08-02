"""Pydantic models for career recommendation flow, exams, and saved careers."""
from typing import Optional
from pydantic import BaseModel, Field


class CareerGuidanceRequest(BaseModel):
    """Input collected from the user on the career-guidance form."""
    name: str = Field(min_length=2, max_length=80)
    age: int = Field(ge=10, le=80)
    education: str  # e.g. "10th", "12th", "Undergraduate", "Postgraduate"
    stream: str  # e.g. "Science", "Commerce", "Arts", "Other"
    percentage: float = Field(ge=0, le=100)
    dream_career: str  # free text; matched against career slugs/aliases


class CareerCompareRequest(BaseModel):
    career_slugs: list[str] = Field(min_length=2, max_length=4)


class SaveCareerRequest(BaseModel):
    career_slug: str
    notes: Optional[str] = None


class StudyPlanCreate(BaseModel):
    career_slug: str
    title: str
    exam_name: Optional[str] = None
    target_date: Optional[str] = None  # ISO date string
    tasks: list[str] = Field(default_factory=list)


class StudyPlanTaskUpdate(BaseModel):
    task_index: int
    completed: bool


class ChatMessageRequest(BaseModel):
    message: str = Field(min_length=1, max_length=1000)
    session_id: Optional[str] = None
