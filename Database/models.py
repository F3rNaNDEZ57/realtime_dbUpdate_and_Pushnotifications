from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, INTEGER, func, Text, DATE, Float
from sqlalchemy.ext.declarative import declarative_base

# this is the base class for the models and it is used to create the tables in the database
base = declarative_base()
metadata = base.metadata


class TestUpdateData(base):
    __tablename__ = "test_update_data"
    id = Column(Integer, primary_key=True)
    value = Column(Integer)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())