from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
import csv
from io import StringIO
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
