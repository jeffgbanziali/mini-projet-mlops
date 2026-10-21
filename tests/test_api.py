from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_predict():
    """Test du préambule : endpoint GET /predict"""
    response = client.get("/predict")
    assert response.status_code == 200
    assert response.json() == {"y_pred": 2}

def test_post_predict_success():
    """Test de l'endpoint POST /predict avec des données valides"""
    payload = {
        "size": 85.5,
        "nb_rooms": 3,
        "garden": 1
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert isinstance(data["prediction"], (int, float))

def test_post_predict_invalid_data():
    """Test de validation : champ manquant ou type incorrect (Pydantic renvoie une 422)"""
    payload = {
        "size": "grande",  # Doit être un float
        "nb_rooms": 3
        # garden manquant
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 422