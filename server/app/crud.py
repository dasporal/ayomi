from sqlalchemy.orm import Session
from . import models

# Function to create a new calculation in the database
def create_calculation(db: Session, operation: str, result: float):
    calc = models.Calculation(operation=operation, result=result)
    db.add(calc)
    db.commit()
    db.refresh(calc)
    return calc

# Function to retrieve all calculations from the database
def get_calculations(db: Session):
    return db.query(models.Calculation).all()
