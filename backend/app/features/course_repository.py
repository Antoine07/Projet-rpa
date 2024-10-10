from sqlalchemy.orm import Session
from app.domain.models import Course 

class CourseRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str):
        course = Course(name=name)
        self.db.add(course)
        self.db.commit()
        self.db.refresh(course)
        return course

    def get_by_id(self, course_id: int):
        return self.db.query(Course).filter(Course.id == course_id).first()

    def get_all(self):
        return self.db.query(Course).all()
