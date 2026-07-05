from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import DocumentResponse
from app.services import search_documents


router = APIRouter()


@router.get("/search", response_model=list[DocumentResponse])
def search(query: str, db: Session = Depends(get_db)):
    return search_documents(db, query)