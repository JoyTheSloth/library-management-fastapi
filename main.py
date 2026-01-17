from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from models.book import Book
from services.library_service import LibraryService
from database.db import create_tables

class BookCreate(BaseModel):
    book_id: int
    title: str
    author: str

app=FastAPI(title="Library Management System")

service=LibraryService()
create_tables()

@app.post("/books")
def add_book(book: BookCreate):
    service.add_book(book)
    return {"message": "Book added successfully"}

@app.get("/books")
def list_books():
    return service.get_books()

@app.post("/books/issue/{book_id}")
def issue_book(book_id:int ):
    if not service.issue_book(book_id):
        raise HTTPException(status_code=400, detail="Book is not available or does not exist")
    
    return {"message": "Book issued successfully"}

@app.post("/books/return/{book_id}")
def return_book(book_id: int):
    if not service.return_book(book_id):
        raise HTTPException(status_code=400, detail="Book does not exist")
    return {"message": "Book returned successfully"}