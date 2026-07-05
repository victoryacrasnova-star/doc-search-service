from elasticsearch import Elasticsearch


ELASTICSEARCH_URL = "http://localhost:9200"

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


if __name__ == "__main__":
    print(check_elasticsearch_connection())