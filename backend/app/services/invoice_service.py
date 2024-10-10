from sqlalchemy.orm import Session
from app.features.invoice_repository import InvoiceRepository
from app.domain.invoice_model import Invoice  

class InvoiceService:
    def __init__(self, db: Session):
        self.invoice_repository = InvoiceRepository(db)

    def get_all_invoices(self) -> list[Invoice]:
        invoices = self.invoice_repository.get_all_invoices()
        
        return [invoice for invoice in invoices]

    def get_invoice_details(self):
        
        return self.invoice_repository.get_invoice_details()
    
    def create_newinvoice(self, invoice_data: dict):
        
         return self.invoice_repository.create_invoice()