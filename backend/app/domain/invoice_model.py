from sqlalchemy import Column, JSON, Integer, String, Numeric, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app.infrastructure.database import Base

class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    invoice_number = Column(String(10), nullable=False)
    creation_date = Column(DateTime, nullable=False)  # Utilisation de DateTime ici
    payment_due = Column(String(50), nullable=False)
    invoice_wording = Column(String(255), nullable=True)
    days_count = Column(Integer, nullable=False)
    hours_count = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)
    tva = Column(Numeric(10, 2), nullable=True)
    amount_ht = Column(Numeric(10, 2), nullable=False)
    amount_ttc = Column(Numeric(10, 2), nullable=False)
    intervention_dates = Column(JSON, nullable=True)
    student_count = Column(Integer, nullable=False)  # Champ pour le nombre d'étudiants

    # Déclaration des clés étrangères avec relations
    school_id = Column(Integer, ForeignKey('schools.id'), nullable=False)  # Relation obligatoire avec la table schools
    trainer_id = Column(Integer, ForeignKey('trainers.id'), nullable=False)  # Relation obligatoire avec la table trainers
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)  # Relation obligatoire avec la table courses
    # Relations
    school = relationship("School", back_populates="invoices")
    trainer = relationship("Trainer", back_populates="invoices")
    course = relationship("Course", back_populates="invoices")
