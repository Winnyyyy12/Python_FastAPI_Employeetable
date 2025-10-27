from pydantic import BaseModel, ConfigDict
#pydantic checks the data types and structure of the data being sent to the API
class EmployeeBase(BaseModel):
    name : str
    position : str
    department : str

#class for creating new employee records
class EmployeeCreate(EmployeeBase):
    id_number:int

#class for reading employee records
class Employee(EmployeeBase):
    id_number:int
    model_config =ConfigDict(from_attributes = True)#enables pydantic to read data from ORM objects like SQLAlchemy models
    #pydantic v2 replacmet for orm_mode=True