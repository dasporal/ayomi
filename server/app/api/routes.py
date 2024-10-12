from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..crud import create_calculation, get_calculations
from ..database import get_db
from ..rpn_calculator import rpn

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "Ayomi"}
  
# Route to calculate RPN and store the result in the database
@router.post("/calculate")
def calculate_rpn(operations: List[str], db: Session = Depends(get_db)):
    result = rpn(operations)
    operation_str = " ".join(operations)
    create_calculation(db, operation=operation_str, result=result)
    return {"result": result}

