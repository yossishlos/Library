from fastapi import APIRouter, HTTPException
from database.book_db import BookDB
from database.db_connection import DB

router = APIRouter(prefix="/books")

db = DB()

book_repository = BookDB(db)

@router.post("")
def create_book(data: dict):
    return book_repository.create_book(data)


@router.get("")
def get_all_books():
    return book_repository.get_all_books()


@router.get("/{id}")
def get_book_by_id(id: int):
    return book_repository.get_book_by_id(id)


@router.put("/{id}")
def update_book(id: int, data: dict):
    return book_repository.update_book(id, data)


@router.put("/{id}/returrn/{member_id}")
def set_available(id: int, val: bool, member_id: int):
    return book_repository.set_available(id, val, member_id)


@router.put("/{id}/borrow/{member_id}")
def set_available(id: int, val: bool, member_id: int):
    return book_repository.set_available(id, val, member_id)
