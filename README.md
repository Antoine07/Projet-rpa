# Proposition d'organisation

## Structure du projet backend avec FastAPI

```txt
features/ 
├── app/
│   ├── features/
│   │   └── api.py                # Points d'entrée API FastAPI
│   ├── domain/
│   │   └── invoice_model.py       # Modèle de données SQLAlchemy pour les factures
│   ├── services/
│   │   └── invoice_service.py     # Logique métier pour la gestion des factures
│   ├── schemas/
│   │   └── invoice_schema.py      # Schémas Pydantic pour la validation des données
│   └── infrastructure/
│       └── database.py            # Configuration de la base de données
│   └── main.py                    # Point d'entrée de l'application
└── requirements.txt               # Dépendances du projet

```
