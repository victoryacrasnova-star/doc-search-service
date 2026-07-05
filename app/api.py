from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import DocumentResponse
from app.services import search_documents


router = APIRouter()


@router.get("/search", response_model=list[DocumentResponse])
def search(query: str, db: Session = Depends(get_db)):
    return search_documents(db, query)

@router.delete("/documents/{document_id}")
def delete_document(document_id: int, db: Session = Depends(get_db)):
    from app.services import delete_document

    success = delete_document(db, document_id)
    if success:
        return {"message": f"Document with ID {document_id} deleted successfully."}
    else:
        return {"message": f"Document with ID {document_id} not found."}