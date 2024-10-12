from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_calculate_rpn():
    response = client.post("/calculate", json=["3", "4", "+", "2", "*"])
    assert response.status_code == 200
    assert response.json() == {"result": 14}

def test_export_csv():
    response = client.get("/export-csv")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]
