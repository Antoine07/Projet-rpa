from sqlalchemy import Column, JSON, Integer, String, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from app.infrastructure.database import Base

class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    invoice_number = Column(String(10), nullable=False)
    client = Column(String(100), nullable=False)
    amount_ht = Column(Numeric(10, 2), nullable=False)
    hours_count = Column(Integer, nullable=False)
    days_count = Column(Integer, nullable=False)
    trainer = Column(String(100), nullable=False)
    trainer_shortcode = Column(String(50), nullable=False)
    payment_due = Column(String(50), nullable=False)
    intervention_dates = Column(JSON, nullable=True)