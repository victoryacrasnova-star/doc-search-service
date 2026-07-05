from app.elastic import search_document_ids
from app.database import delete_document_from_db, get_documents_by_ids
from app.elastic import delete_document_from_index


def search_documents(db, query: str):
    document_ids = search_document_ids(query)
    return get_documents_by_ids(db, document_ids)

def delete_documents(db, document_id: int):

    success = delete_document_from_db(db, document_id)
    if success:
        delete_document_from_index(document_id)
    return success