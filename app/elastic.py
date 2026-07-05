import os

from elasticsearch import Elasticsearch

ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")

es_client = Elasticsearch(ELASTICSEARCH_URL)

def check_elasticsearch_connection():
    return es_client.info()

def index_document(document_id: int, text: str):
    document = {
        "text": text
    }
    es_client.index(index="documents", id=document_id, document=document)

def search_document_ids(query: str, limit: int = 20) -> list[int]:
    response = es_client.search(
        index="documents",
        query={
            "match": {
                "text": query
            }
        },
        size=limit,
    )

    hits = response["hits"]["hits"]

    return [int(hit["_id"]) for hit in hits]


def delete_document_from_index(document_id):
    es_client.delete(index="documents", id=document_id)
