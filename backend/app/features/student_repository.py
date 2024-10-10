from sqlalchemy.orm import Session
from app.domain.stutden_model import Student

class StudentRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, email: str, school_id: int):
        student = Student(name=name, email=email, school_id=school_id)
        self.db.add(student)
        self.db.commit()
        self.db.refresh(student)
        return student

    def get_by_id(self, student_id: int):
        return self.db.query(Student).filter(Student.id == student_id).first()

    def get_all(self):
        return self.db.query(Student).all()
