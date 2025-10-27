from sqlalchemy import create_engine  #create_engine-bridge between python and database
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
#declaratice_base()--creates a base class that all the tables(models) will inherit from
#DeclarativeMeta()--it helps sqlalchemy to understand the tables class structure
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./employees.db" #database address

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={
    "check_same_thread": False}) #allow multiple threads to access the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #bind=engine--tells the session which databse to use
Base: DeclarativeMeta = declarative_base()  #Base--parent class for all the models(tables) in the database