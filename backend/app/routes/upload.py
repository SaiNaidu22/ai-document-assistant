from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.config import UPLOAD_FOLDER
from app.services.pdf_service import extract_text
from app.services.chunk_service import create_chunks
from app.services.embedding_service import generate_embedding
from app.services.vector_store import store_chunks

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    extracted_text = extract_text(file_path)

    # Create chunks
    chunks = create_chunks(extracted_text)

    # Generate embeddings
    embeddings = []

    for chunk in chunks:
        embedding = generate_embedding(chunk)
        embeddings.append(embedding)

    # Store in ChromaDB
    store_chunks(chunks, embeddings)

    return {
        "filename": file.filename,
        "characters": len(extracted_text),
        "chunks": len(chunks),
        "preview": chunks[:3],
        "message": "Document stored successfully!"
    }