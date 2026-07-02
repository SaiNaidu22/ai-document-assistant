from fastapi import APIRouter
from pydantic import BaseModel

from app.services.embedding_service import generate_embedding
from app.services.vector_store import search_chunks
from app.services.rag_service import generate_answer

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    question_embedding = generate_embedding(
        request.question
    )

    retrieved_chunks = search_chunks(
        question_embedding
    )

    context = "\n\n".join(retrieved_chunks)

    answer = generate_answer(
        request.question,
        context
    )

    return {
        "question": request.question,
        "answer": answer,
        "sources": retrieved_chunks
    }