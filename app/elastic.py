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


if __name__ == "__main__":
    print(check_elasticsearch_connection())