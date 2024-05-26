from sqlalchemy import Column, String, Text, Integer

# database.py에서 생성한 Base import

from database import Base


# 상속 받아 SQLAlchemy model 생성


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=True)
    time = Column(String, nullable=True)
    location = Column(String, nullable=True)
    description = Column(Text, nullable=True)