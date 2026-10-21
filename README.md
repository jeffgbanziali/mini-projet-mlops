# Deploiement d'un Modele de Machine Learning avec FastAPI et Docker

Ce projet presente le cycle complet de mise en production d'un modele de regression lineaire pour l'estimation de prix immobiliers, allant du prototypage applicatif jusqu'au deploiement conteneurise sur une machine virtuelle distante.

---

## 1. Structure du projet

```text
mini-projet-ml/
├── Dockerfile              # Instructions de conteneurisation Docker
├── requirements.txt        # Dependances Python du projet
├── regression.joblib       # Modele de regression entraine
├── model_app.py            # API REST developpee avec FastAPI
└── tests/
    └── test_api.py         # Tests unitaires executes avec pytest
```

---

## 2. Dependances principales

Le projet repose sur les bibliotheques suivantes :
- `fastapi` et `uvicorn` : creation et execution du serveur d'API REST.
- `pydantic` : validation des donnees entrantes (payload JSON).
- `scikit-learn`, `joblib`, `pandas`, `numpy` : chargement et inference du modele ML.
- `pytest`, `httpx` : tests unitaires et validation des endpoints.

---

## 3. Endpoints de l'API

L'application expose deux endpoints principaux sur `/predict` :

1. **GET `/predict`**
   - Verification basique du statut de l'API.
   - Reponse : `{"y_pred": 2}`

2. **POST `/predict`**
   - Realise la prediction a partir des caracteristiques fournies.
   - Corps de la requete (JSON) :
     ```json
     {
       "size": 95.0,
       "nb_rooms": 4,
       "garden": 1
     }
     ```
   - Reponse (JSON) :
     ```json
     {
       "prediction": 308 855,23,
     }
     ```

---

## 4. Etapes realisees

### Niveau 0 : Developpement et tests locaux
- Entrainement et serialisation du modele sous `regression.joblib`.
- Ecriture de l'application FastAPI dans `model_app.py`.
- Validation du bon fonctionnement a l'aide de tests unitaires automatises :
  ```bash
  python -m pytest
  ```

### Niveau 0.5 : Deploiement direct sur machine distante (SSH)
- Connexion SSH a la machine distante Ubuntu.
- Transfert securise des fichiers necessaires (`model_app.py`, `regression.joblib`, `requirements.txt`) via `scp`.
- Installation des dependances Python.
- Execution du serveur Uvicorn lie a toutes les interfaces (`0.0.0.0`) sur un port dedie.
- Verification des requetes GET et POST depuis la machine locale.

### Niveau 1 : Conteneurisation locale avec Docker
- Redaction du fichier `Dockerfile` base sur l'image `python:3.10-slim`.
- Construction de l'image Docker locale :
  ```bash
  docker build -t ml-house-predictor:v1 .
  ```
- Lancement et mappage des ports en local :
  ```bash
  docker run -d -p 8000:8000 --name mon-serveur-ml ml-house-predictor:v1
  ```
- Validation des requetes HTTP sur `http://localhost:8000`.

### Niveau 2 : Deploiement conteneurise sur machine virtuelle cloud
- Transfert du `Dockerfile` et du code vers le repertoire distant `~/jg-efrei/`.
- Construction de l'image Docker directement sur la machine distante :
  ```bash
  docker build -t jg-ml-app:latest .
  ```
- Demarrage du conteneur en arriere-plan avec redemarrage automatique :
  ```bash
  docker run -d -p 8990:8000 --name mon-serveur-ml-docker --restart always jg-ml-app:latest
  ```
- Validation finale des appels HTTP distants :
  ```powershell
  Invoke-RestMethod -Uri http://40.66.48.24:8990/predict -Method Post -ContentType "application/json" -Body '{"size": 95.0, "nb_rooms": 4, "garden": 1}'
  ```
