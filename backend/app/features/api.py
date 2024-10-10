from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.invoice_schema import InvoiceResponse
from app.services.invoice_service import InvoiceService
from app.infrastructure.database import get_db

router = APIRouter()

@router.get("/invoices", response_model=list[InvoiceResponse])
def get_invoices(db: Session = Depends(get_db)):
    invoice_service = InvoiceService(db)
    invoices = invoice_service.get_all_invoices()
    
    return invoices

@router.get("/invoices/details", response_model=list[InvoiceResponse])
def get_invoice_details(db: Session = Depends(get_db)):
    invoice_repository = InvoiceService(db)
    invoices = invoice_repository.get_invoice_details()
    
    return invoices