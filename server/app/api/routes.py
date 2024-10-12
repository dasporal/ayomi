from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
import csv
from io import StringIO
from typing import List, Union
from ..crud import create_calculation, get_calculations
from ..database import get_db
from ..rpn_calculator import rpn
from pydantic import BaseModel

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "Ayomi"}

class CalculationRequest(BaseModel):
    stack: List[Union[float, str]] 
  
# Route to calculate RPN and store the result in the database
@router.post("/calculate")
def calculate_rpn(operations: List[Union[float, str]], db: Session = Depends(get_db)):
    try:
        result = rpn(operations)  # Call the rpn function with the list of operations
        operation_str = " ".join(map(str, operations))  # Convert the list to a string for logging
        create_calculation(db, operation=operation_str, result=result)  # Save to the database
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Route to export all calculations to CSV
@router.get("/export-csv")
def export_csv(db: Session = Depends(get_db)):
    calculations = get_calculations(db)
    
    output = StringIO()
    writer = csv.writer(output, delimiter=';')
    writer.writerow(["ID", "Operation", "Result", "Timestamp"])
    
    for calc in calculations:
        writer.writerow([calc.id, calc.operation, calc.result, calc.timestamp])

    output.seek(0)
    
    return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=calculations.csv"})
