from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.models import QuestionCreate, Question, QuestionRead
from src.database.session import session_scope
from dotenv import load_dotenv
import aiohttp
import requests

router = APIRouter(
    prefix="questions",
    tags="question"
)

# def get_unique_question():
#     url = "https://jservice.io/api/random?count=1"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         question = data[0]
#         if question in database:
#             return get_unique_question()
#         else:
#             return Question(
#                 question_id=question["id"],
#                 question_text=question["question"],
#                 answer_text=question["answer"],
#                 created_date=question["created_at"]
#             )
#     raise HTTPException(status_code=500, detail="Failed to get quiz question")
# def get_last_question(model: ModelQuestion = ModelQuestion) -> ModelQuestion:
#     return db.session.query(model).order_by(model.id.desc()).first()

# @router.post("/")
# def get_quiz_questions(request: QuestionRead):
#     questions_num = request.questions_num
#     for _ in range(questions_num):
#         question = get_unique_question()
#         database.append(question)
#     return database[-questions_num:]

# @router.post("/", response_model=QuetionCreate)
# async def take_quation(questions_num: int, session: AsyncSession = Depends(session_scope)):
#     entity = Question(
#         question_id=user.username,
#         hashed_password=user.hashed_password,
#         email=user.email
#     )
#     session.add(entity)
#     await session.commit()
#     await session.refresh(entity)
#     return entity
