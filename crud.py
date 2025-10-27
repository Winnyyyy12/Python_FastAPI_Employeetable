from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import text
import models, schemas


# fetch a single employee by id_number
def get_employee(db: Session, id_number: int):
    return db.query(models.Employee).filter(models.Employee.id_number == id_number).first()
# db.query(models.Employee)--start a query on the employee table
# .filter(models.Employee.id_number == id_number)--only select rows where id_number matches
# .first()--get the first result of the query


# fetch multiple employees
# skip-number of rows to skip; limit-max row in return;
def get_employees(db: Session, skip: int = 0, limit: int = 10, department: str | None = None):
    query = db.query(models.Employee)
    if department:
        query = query.filter(models.Employee.department == department)
    # Without .all(), SQLAlchemy just keeps it as a query object, nothing is fetched yet
    return query.offset(skip).limit(limit).all()
# .offset(skip)-skips the first 'skip' rows
# .limit(limit)-limits the result to 'limit' rows
# .all()-fetches all the results of the query as a list


# function to create a new employee
# employee:schemas.EmployeeCreate--data validation using pydantic schema
def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        id_number=employee.id_number,
        name=employee.name,
        position=employee.position,
        department=employee.department
    )
    db.add(db_employee)  # adds the new employee instance to the database session
    db.commit()  # commits the transaction to the database
    # refreshes the instance with the data from the database
    db.refresh(db_employee)
    return db_employee


# function to delete an employee by id_number
def delete_employee(db: Session, id_number: int):
    employee = db.query(models.Employee).filter(
        models.Employee.id_number == id_number).first()
    if employee:
        db.delete(employee)
        db.commit()
        return True
    return False
