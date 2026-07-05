import csv
from pathlib import Path
from app.models import Document
from app.elastic import index_document
import ast
from datetime import datetime
from app.database import SessionLocal


CSV_PATH = Path("data/posts.csv")

def parse_rubrics(value: str) -> str:
    rubrics = ast.literal_eval(value)
    return ", ".join(rubrics)

def parse_created_date(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")

def load_csv():
    db = SessionLocal()
    try:
        with CSV_PATH.open("r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            documents = []

            for row in reader:
                rubrics = parse_rubrics(row["rubrics"])
                created_date = parse_created_date(row["created_date"])


                document = Document(
                    rubrics=rubrics,
                    text=row["text"],
                    created_date=created_date,
                )
                db.add(document)
                documents.append(document)
            db.commit()

            for document in documents:
                db.refresh(document)
                index_document(document.id, document.text)

    finally:
        db.close()

if __name__ == "__main__":
    load_csv()