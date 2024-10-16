from sqlalchemy.orm import Session
from app.domain.invoice_model import Invoice
from app.schemas.invoice_schema import InvoiceCreate
from sqlalchemy import func

class InvoiceRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all_invoices(self) -> list[Invoice]:
        return self.db.query(Invoice).all()

    def get_invoice_details(self):
        invoices = self.db.query(Invoice).join(Invoice.school).join(Invoice.trainer).join(Invoice.course).all()
        
        results = []
        for invoice in invoices:
            results.append({
                "invoice_number": invoice.invoice_number,
                "creation_date": invoice.creation_date.isoformat(),
                "invoice_wording": invoice.invoice_wording,
                "days_count": invoice.days_count,
                "hours_count": invoice.hours_count,
                "unit_price": invoice.unit_price,
                "tva": invoice.tva,
                "amount_ht": invoice.amount_ht,
                "amount_ttc": invoice.amount_ttc,
                "intervention_dates": invoice.intervention_dates,
                "student_count": invoice.student_count,
                "school_name": invoice.school.name, 
                "course_name": invoice.course.name,  
        })
            
        return results

    def create_invoice(db: Session, invoice: InvoiceCreate):
        course = db.query(Course).filter(Course.id == invoice.course_id).first()
        if not course:
            raise ValueError("Course not found")

        # Calcul du nombre d'étudiants inscrits au cours
        student_count = len(course.students)

        db_invoice = Invoice(
            invoice_number=invoice.invoice_number,
            creation_date=invoice.creation_date,
            payment_due=invoice.payment_due,
            invoice_wording=invoice.invoice_wording,
            days_count=invoice.days_count,
            hours_count=invoice.hours_count,
            unit_price=invoice.unit_price,
            tva=invoice.tva,
            amount_ht=invoice.amount_ht,
            amount_ttc=invoice.amount_ttc,
            intervention_dates=invoice.intervention_dates,
            student_count=student_count,  # Nombre d'étudiants calculé
            school_id=invoice.school_id,
            trainer_id=invoice.trainer_id,
            course_id=invoice.course_id
        )
        db.add(db_invoice)
        db.commit()
        db.refresh(db_invoice)
        return db_invoice

    def get_amountInvoice(self):
        return self.db.query(func.sum(Invoice.amount_ttc)).scalar() or 0
    
    def get_totalStudentInvoice(self):
         return self.db.query(func.sum(Invoice.student_count)).scalar() or 0