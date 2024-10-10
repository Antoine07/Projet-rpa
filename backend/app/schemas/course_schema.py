from pydantic import BaseModel
from typing import List, Optional

class CourseBase(BaseModel):
    name: str
    subject_id: int  # ID de la matière associée

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int
    trainers: List[int] = []  # Liste des IDs des formateurs associés

    class Config:
        from_attributes = True  # Nouveau nom

class CourseResponse(CourseBase):
    id: int
    trainers: List[int] = []  # Liste des IDs des formateurs associés

    class Config:
        from_attributes = True  # Nouveau nom
