from sqlalchemy.orm import Session
from app.features.repositories.invoice_repository import InvoiceRepository
from app.domain.invoice_model import Invoice  # Importez le modèle SQLAlchemy

class InvoiceService:
    def __init__(self, db: Session):
        self.invoice_repository = InvoiceRepository(db)

    def get_all_invoices(self) -> list[Invoice]:
        invoices = self.invoice_repository.get_all_invoices()
        
        return [invoice for invoice in invoices]
