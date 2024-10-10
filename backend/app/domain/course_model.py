from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    # Relations
    # Relation avec la table des factures (invoices)
    invoices = relationship("Invoice", back_populates="course")

    trainers = relationship("Trainer", secondary='course_trainers', back_populates="courses")  # N:N avec Trainers
    students = relationship("Student", secondary="student_courses", back_populates="courses")  # Assurez-vous que 'student_courses' est correctement défini