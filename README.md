# Proposition d'organisation

## Structure du projet

```txt
├── app
│   ├── features
│   │   ├── api.py                   # Points d'entrée API FastAPI
│   │   ├── invoice_repository.py     # Repositories pour la gestion DB des factures
│   │   ├── user_repository.py        # Repositories pour la gestion DB des utilisateurs
│   ├── domain
│   │   ├── invoice_models.py         # Modèles de factures
│   │   └── user_models.py            # Modèles des utilisateurs
│   ├── infrastructure
│   │   └── database.py               # Configuration de la base de données
│   ├── services
│   │   └── invoice_service.py        # Logique métier pour les factures
│   ├── schemas                       # Dossier pour les schémas Pydantic
│   │   ├── invoice_schema.py         # Schémas Pydantic pour les factures
│   │   └── user_schema.py            # Schémas Pydantic pour les utilisateurs
│   └── main.py                       # Point d'entrée de l'application
├── tests
│   ├── test_invoices.py              # Tests pour le module de factures
│   ├── test_users.py                 # Tests pour le module des utilisateurs
└── Dockerfile
└── .env
└── requirements.txt


```