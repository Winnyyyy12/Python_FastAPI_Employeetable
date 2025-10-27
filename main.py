from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

# creates the database tables based on the models defined in models.py
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee API")


def get_db():
    db = SessionLocal()  #creates a new database session
    try:
        yield db
    finally:
        db.close()


@app.post("/employees/", response_model=schemas.Employee)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, id_number=employee.id_number)
    if db_employee:
        raise HTTPException(
            status_code=400, detail="Employee with this ID already exists")
    return crud.create_employee(db=db, employee=employee)


@app.get("/employees/{id_number}", response_model=schemas.Employee)
def read_employee(id_number: int, db: Session = Depends(get_db)):
    db_employee = crud.get_employee(db, id_number=id_number)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee


@app.get("/employees/", response_model=List[schemas.Employee])
def list_employees(skip: int = 0, limit: int = 10, department: str | None = None, db: Session = Depends(get_db)):
    return crud.get_employee(db, skip=skip, limit=limit, department=department)


@app.delete("/employees/{id_number}", response_model=dict)
def delete_employee(id_number: int, db: Session = Depends(get_db)):
    deleted = crud.delete_employee(db, id_number=id_number)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"detail": "Employee deleted successfully"}
