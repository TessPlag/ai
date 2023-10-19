import uvicorn
from fastapi import FastAPI
from src.routers import router

app = FastAPI(
    title="AI"
)

app.include_router(
    router,
    tags=["Question"]
)

if __name__ == '__main__':
    uvicorn.run(app)
