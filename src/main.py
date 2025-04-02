from fastapi import FastAPI
from src.api import router

app = FastAPI(
    title="Promtior Chatbot API",
    description="Ask questions based on internal company documentation.",
    version="1.0.0"
)

app.include_router(router)
