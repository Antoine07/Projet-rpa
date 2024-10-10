from sqlalchemy.orm import Session
from sqlalchemy import func

from app.domain.trainer_model import Trainer
from app.domain.invoice_model import Invoice
from app.domain.school_model import School

from app.domain.types import TrainerPerSchoolType
from typing import List

class TrainerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, shortcode: str):
        trainer = Trainer(name=name, shortcode=shortcode)
        self.db.add(trainer)
        self.db.commit()
        self.db.refresh(trainer)
        return trainer

    def get_by_id(self, trainer_id: int):
        return self.db.query(Trainer).filter(Trainer.id == trainer_id).first()

    def get_all(self):
        return self.db.query(Trainer).all()

    def get_trainers_per_school(self) -> List[TrainerPerSchoolType]:
        
        results = self.db.query(
            Trainer.name.label("trainer_name"),
            School.name.label("school_name"),
            func.sum(Invoice.student_count).label("total_students")
        ).select_from(Invoice).join(School, Invoice.school_id == School.id).join(Trainer, Invoice.trainer_id == Trainer.id).group_by(School.name, Trainer.name).all()

        return [
            TrainerPerSchoolType(
                trainer_name=r.trainer_name,
                school_name=r.school_name,
                total_students=r.total_students
            ) for r in results
        ]
