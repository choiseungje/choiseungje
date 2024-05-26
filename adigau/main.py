from fastapi import FastAPI

from models import Base
from database import engine
from domain.items import items_router

Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
app.include_router(items_router.router)
