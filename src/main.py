import uvicorn
from fastapi import FastAPI
from src.routers import routers

app = FastAPI(
    title="AI"
)

app.include_router(
    routers,
    tags=["Question"]
)

if __name__ == '__main__':
    uvicorn.run(app)
