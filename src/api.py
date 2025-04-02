from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.gemini_client import query_gemini

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

@router.post("/ask", tags=["Chat"])
async def ask_question(request: QuestionRequest):
    try:
        response = query_gemini(request.question)
        return {"question": request.question, "answer": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
