import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def get_documents_by_ids(db, document_ids: list[int]):

    from app.models import Document

    
    if not document_ids:
        return []

    return (
        db.query(Document)
        .filter(Document.id.in_(document_ids))
        .order_by(Document.created_date.desc())
        .limit(20)
        .all()
    )

def delete_document_from_db(db, document_id):
    from app.models import Document

    document = db.query(Document).filter(Document.id == document_id).first()
    if document:
        db.delete(document)
        db.commit()
        return True
    return False