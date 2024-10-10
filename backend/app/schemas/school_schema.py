from pydantic import BaseModel
from typing import List, Optional

class SchoolBase(BaseModel):
    name: str

class SchoolCreate(SchoolBase):
    pass

class School(SchoolBase):
    id: int
    students: List[Optional['Student']] = []  # Liste des étudiants associés (peut être vide)
    invoices: List[Optional['Invoice']] = []  # Liste des factures associées (peut être vide)

    class Config:
        from_attributes = True  # Nouveau nom

# Pour permettre la référence d'autodocumentation dans le modèle
School.update_forward_refs()
