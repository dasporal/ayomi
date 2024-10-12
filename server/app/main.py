from fastapi import FastAPI
from .database import engine
from .models import Base
from .api import routes

Base.metadata.create_all(bind=engine)

app = FastAPI(
  title="My RPN Calculator API for Ayomi",
  description="An API to perform RPN calculations and export calculation history.",
  version="1.0.0",
)

app.include_router(routes.router)