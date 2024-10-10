from sqlalchemy.orm import Session
from sqlalchemy import func
from app.domain.student_model import Student
from app.domain.trainer_model import Trainer
from app.domain.student_model import Student

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

    def get_totalStudent(self):
        result = (
        self.db.query(
                Trainer.name.label("trainer_name"),
                School.name.label("school_name"),
                func.count(Student.id).label("total_students")  # Compte le nombre d'étudiants
            )
                .select_from(Course)  # Joindre la table des cours
                .join(Trainer)  # Joindre la table des formateurs
                .join(School)  # Joindre la table des écoles
                .join(Student, Student.course_id == Course.id)  # Joindre la table des étudiants
                .group_by(Trainer.name, School.name)  # Grouper par formateur et école
                .all()
            )
        
        # Retourne une liste des résultats et le total
        return {
            "total_students": total_students,
            "details": [
                {
                    "trainer_name": result.trainer_name,
                    "school_name": result.school_name,
                    "total_students": result.total_students
                }
                for result in results
            ]
        }
