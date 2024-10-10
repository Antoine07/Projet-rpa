from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app.infrastructure.database import Base

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    school_id = Column(Integer, ForeignKey('schools.id'), nullable=True)

    # Relations
    school = relationship("School", back_populates="students")  # Relation avec l'école
    courses = relationship("Course", secondary='student_courses', back_populates="students")  # Relation N:N avec les cours
