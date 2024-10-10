from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app.infrastructure.database import Base

class School(Base):
    __tablename__ = 'schools'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    # Relations
    students = relationship("Student", back_populates="school")  # Relation avec les étudiants
    invoices = relationship("Invoice", back_populates="school")  # Relation avec les factures
    trainers = relationship("Trainer", secondary='trainer_schools', back_populates="schools")  # Relation N:N avec les formateurs

