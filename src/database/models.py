from typing import Optional

from pydantic import BaseModel, ConfigDict
from sqlalchemy import ForeignKey, String, Enum, func
from sqlalchemy.orm import mapped_column, Mapped
from datetime import datetime
from src.database.base import Base
# from src.database.utils import as_form


class Question(Base):
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)
    question_id: Mapped[int] = mapped_column(nullable=False )
    questions: Mapped[str] = mapped_column(default=False, nullable=False)
    answers: Mapped[str] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(nullable=False, default=func.now())
    

# @as_form
class QuestionCreate(BaseModel):
    question_id: int
    questions: str
    answers: str

    model_config = ConfigDict(from_attributes=True)


class QuestionRead(BaseModel):
    quation_id: str

    model_config = ConfigDict(from_attributes=True)
