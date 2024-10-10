from pydantic import BaseModel

class TrainerBase(BaseModel):
    name: str  # Nom du formateur, doit être une chaîne de caractères
    shortcode: str  # Code abrégé du formateur, utilisé pour l'identification

class TrainerCreate(TrainerBase):
    pass  # Classe pour la création d'un nouveau formateur

class Trainer(TrainerBase):
    id: int  # Identifiant unique du formateur

    class Config:
        from_attributes = True  # Nouveau nom

# Pour permettre la référence d'autodocumentation dans le modèle
Trainer.update_forward_refs()
