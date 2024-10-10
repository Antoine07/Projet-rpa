from sqlalchemy import Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.infrastructure.database import Base

# Table d'association pour la relation N:N entre Courses et Trainers
course_trainers = Table(
    'course_trainers',
    Base.metadata,
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True),
    Column('trainer_id', Integer, ForeignKey('trainers.id'), primary_key=True)
)

# Table intermédiaire pour la relation N:N entre les étudiants et les cours
student_course = Table('student_courses', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('courses.id'), primary_key=True)
)

# Table d'association pour la relation N:N entre Trainers et Schools
trainer_schools = Table(
    'trainer_schools',
    Base.metadata,
    Column('trainer_id', Integer, ForeignKey('trainers.id'), primary_key=True),
    Column('school_id', Integer, ForeignKey('schools.id'), primary_key=True)
)