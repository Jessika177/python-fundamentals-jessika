from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import json

class Document(BaseModel):
    id: int
    title: str
    tags: Optional[List[str]] = None
    views: Optional[int] = None
    published: Optional[bool] = None
    metadata: Optional[Dict[str, Any]] = None

def load_documents(filepath: str) -> List[Document]:
    with open(filepath, "r", encoding="utf-8") as file:
        records = json.load(file)
    documents = [Document(**record) for record in records]
    return documents

def display_document(doc: Document) -> None:
    print(f"ID: {doc.id}")
    print(f"Title: {doc.title}")
    print(f"Tags: {doc.tags if doc.tags else 'No tags'}")
    print(f"Views: {doc.views if doc.views is not None else 'No view count'}")
    print(f"Published: {doc.published if doc.published is not None else 'Unknown'}")
    print(f"Metadata: {doc.metadata if doc.metadata else 'No metadata'}")
    print("-" * 40)

if __name__ == "__main__":
    filepath = "data/documents.json"
    documents = load_documents(filepath)
    for doc in documents:
        display_document(doc)
