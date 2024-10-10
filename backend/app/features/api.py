from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.invoice_schema import InvoiceResponse
from app.services.invoice_service import InvoiceService
from app.infrastructure.database import get_db
from app.services.bpf_service import BpfService
from app.domain.types import BpfType

router = APIRouter()

@router.get("/invoices", response_model=list[InvoiceResponse])
def get_invoices(db: Session = Depends(get_db)):
    invoice_service = InvoiceService(db)
    invoices = invoice_service.get_all_invoices()
    
    return invoices

@router.get("/invoices/details", response_model=None)
def get_invoice_details(db: Session = Depends(get_db)):
    invoice_service = InvoiceService(db)
    invoices = invoice_service.get_invoice_details()
    
    return invoices

@router.get("/invoices/bpf", response_model=None)
def get_invoice_details(db: Session = Depends(get_db)):
    bpf = BpfService(db)
    
    return bpf.get_bpf()