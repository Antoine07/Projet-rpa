from sqlalchemy.orm import Session
from app.features.invoice_repository import InvoiceRepository
from app.features.trainer_repository import TrainerRepository
from app.features.student_repository import StudentRepository
from app.domain.invoice_model import Invoice 

from app.domain.types import BpfType
from typing import List

class BpfService:
    def __init__(self, db: Session):
        self.invoice_repository = InvoiceRepository(db)
        self.trainer_repository = TrainerRepository(db)
        self.student_repository = StudentRepository(db)

    def get_bpf(self)->List[BpfType]:
        amount = self.invoice_repository.get_amountInvoice()
        totalStudent = self.invoice_repository.get_totalStudentInvoice()
        
        return {
            "amount" : amount,
            "totalStudent" : totalStudent,
             "trainer_per_school" : self.trainer_repository.get_trainers_per_school()
        }
