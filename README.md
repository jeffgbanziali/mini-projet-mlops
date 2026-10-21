# Mini-projet : modèle ML de prix de maisons

## Étape 1 : Streamlit

```bash
pip install -r requirements.txt
python train_model.py    # génère regression.joblib
streamlit run model_app.py
```

Ouvrir http://localhost:8501

## Suite
- Niveau 0 : API FastAPI (GET puis POST /predict)
- Niveau 0.5 : déploiement sur machine distante
- Niveau 1 : Dockerfile
- Niveau 2 : conteneur sur VM cloud
