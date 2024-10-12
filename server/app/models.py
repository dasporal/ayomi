from sqlalchemy import Column, Integer, Float, String, DateTime
from .database import Base
import datetime

# SQLAlchemy model for the Calculations table
class Calculation(Base):
    __tablename__ = "calculations"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, index=True)
    result = Column(Float)
    timestamp = Column(DateTime, default=datetime.timezone.utc)