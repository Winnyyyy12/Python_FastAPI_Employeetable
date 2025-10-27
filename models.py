from sqlalchemy import Column, Integer, String
from database import Base  #importing the Base class from database.py

class Employee(Base):
    __tablename__ = "employees" #name of the table in the database(the underscores are used to avoid name conflicts)
    
    id_number = Column(Integer, primary_key=True, index=True) #primary_key=True--uniquely identifies each record in the table; Index=True--helps the database find things faster
    name = Column(String, nullable=False) #nullable=False--this field cannot be left empty
    position = Column(String, nullable=False)
    department = Column(String, nullable=False)