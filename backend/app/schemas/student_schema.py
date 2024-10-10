from pydantic import BaseModel, EmailStr
from typing import Optional

class StudentBase(BaseModel):
    name: str
    email: EmailStr  # Utilisation de EmailStr pour une validation d'email

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    school_id: Optional[int]  # ID de l'école associée, peut être None si non attribuée

    class Config:
        from_attributes = True  # Nouveau nom

# Pour permettre la référence d'autodocumentation dans le modèle
Student.update_forward_refs()
