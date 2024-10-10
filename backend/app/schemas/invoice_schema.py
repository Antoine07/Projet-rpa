from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from decimal import Decimal

class InterventionDate(BaseModel):
    start_date: datetime  # Date de début de l'intervention
    end_date: datetime  # Date de fin de l'intervention

class InvoiceBase(BaseModel):
    invoice_number: str  # Numéro de la facture
    creation_date: datetime  # Date de création
    payment_due: str  # Date d'échéance (garder en tant que string si nécessaire)
    invoice_wording: Optional[str] = None  # Description de la facture
    days_count: int  # Nombre de jours
    hours_count: int  # Nombre d'heures
    unit_price: Decimal  # Prix unitaire
    tva: Optional[Decimal] = None  # TVA (optionnelle)
    amount_ht: Decimal  # Montant hors taxes
    amount_ttc: Decimal  # Montant toutes taxes comprises
    intervention_dates: Optional[List[InterventionDate]] = None  # Dates d'intervention sous forme de liste d'objets
    student_count: int  # Nombre d'étudiants
    school_id: int  # ID de l'école
    trainer_id: int  # ID du formateur
    course_id: int  # ID du cours

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int  # ID de la facture

    class Config:
        from_attributes = True  # Permet l'attribution des valeurs à partir des attributs

class HealthResponse(BaseModel):
    status: str

class InvoiceResponse(InvoiceBase):
    id: int  # ID de la facture

    class Config:
        from_attributes = True  # Permet l'attribution des valeurs à partir des attributs
