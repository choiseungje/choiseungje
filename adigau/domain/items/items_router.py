from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from domain.items import items_schema, items_crud
from database import get_db

router = APIRouter(
    prefix="/api/items",
)


@router.get("/list", response_model=list[items_schema.ItemBase])
def items_list(db: Session = Depends(get_db)):
    _items_list = items_crud.get_items_list(db)
    return _items_list
