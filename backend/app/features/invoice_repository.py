from sqlalchemy.orm import Session
from app.domain.invoice_model import Invoice

class InvoiceRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_invoices(self) -> list[Invoice]:
        return self.db.query(Invoice).all()
