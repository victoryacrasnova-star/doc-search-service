from datetime import datetime
from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: int
    rubrics: str
    text: str
    created_date: datetime

    class Config:
        from_attributes = True