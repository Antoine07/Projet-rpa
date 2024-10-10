from sqlalchemy.orm import Session
from app.domain.trainer_model import Trainer

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
