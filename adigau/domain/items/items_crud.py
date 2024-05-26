from sqlalchemy.orm import Session
from models import Item
from domain.items.items_schema import ItemBase


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: ItemBase):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_items_list(db: Session):
    items_list = db.query(Item)\
        .all()
    return items_list