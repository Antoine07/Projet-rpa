from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.features.api import router as api_router
from app.infrastructure.database import SessionLocal, engine, Base

from app.domain.base_model import course_trainers, student_course, trainer_schools
from app.domain.invoice_model import Invoice
from app.domain.school_model import School
from app.domain.student_model import Student
from app.domain.trainer_model import Trainer
from app.domain.course_model import Course

app = FastAPI(title="Invoice API")

# Configurer CORS si nécessaire
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Créer toutes les tables dans la base de données
@app.on_event("startup")
async def startup():
    # Créez les tables en fonction de vos modèles
    Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome to the Invoice API !"}

# Inclure les routes de l'API
app.include_router(api_router, prefix="/api", tags=["invoices"])

# Route de santé pour vérifier que l'API fonctionne
@app.get("/health")
async def health():
    return {"status": "Healthy"}
