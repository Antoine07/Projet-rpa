from sqlalchemy.orm import Session
from app.domain.base import course_trainers as CourseTrainer

class CourseTrainerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, course_id: int, trainer_id: int):
        course_trainer = CourseTrainer(course_id=course_id, trainer_id=trainer_id)
        self.db.add(course_trainer)
        self.db.commit()
        return course_trainer
