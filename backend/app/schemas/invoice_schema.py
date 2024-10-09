from pydantic import BaseModel
from typing import Dict, Union
from datetime import datetime

class InvoiceBase(BaseModel):
    invoice_number: str
    client: str
    amount_ht: float
    hours_count: int
    days_count: int
    trainer: str
    trainer_shortcode: str
    payment_due: str
    intervention_dates : Dict[str, Union[str, datetime]]

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int

    class Config:
        orm_mode = True

class HealthResponse(BaseModel):
    status: str
    
class InvoiceResponse(InvoiceBase):
    id: int

    class Config:
        orm_mode = True