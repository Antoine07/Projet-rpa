from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app.infrastructure.database import Base

class Trainer(Base):
    __tablename__ = 'trainers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    shortcode = Column(String(50), nullable=False)

    # Relations
    invoices = relationship("Invoice", back_populates="trainer")
    schools = relationship("School", secondary="trainer_schools", back_populates="trainers")  # N:N avec Schools
    courses = relationship("Course", secondary="course_trainers", back_populates="trainers")