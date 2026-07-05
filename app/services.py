

from app.elastic import search_document_ids
from app.database import get_documents_by_ids


def search_documents(db, query: str):
    document_ids = search_document_ids(query)
    return get_documents_by_ids(db, document_ids)