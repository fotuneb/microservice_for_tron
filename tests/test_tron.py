# tests/test_tron.py
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.tron_service import TronService
from app.db.session import SessionLocal
from app.db.models import TronQuery
from unittest.mock import patch

# Тестирование POST запроса
@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

# Тестируем POST /tron
def test_get_tron_data(client):
    # Мокируем TronService
    mock_tron_data = {
        "address": "TXYZ1234567890",
        "balance": 100.0,
        "bandwidth": 1000,
        "energy": 500,
    }
    
    # Мокаем метод get_account_info и save_query
    with patch.object(TronService, "get_account_info", return_value=mock_tron_data), \
         patch.object(TronService, "save_query", return_value=mock_tron_data):
        
        response = client.post("/tron", json={"address": "TXYZ1234567890"})
        
        assert response.status_code == 200
        data = response.json()
        assert data["address"] == "TXYZ1234567890"
        assert data["balance"] == 100.0
        assert data["bandwidth"] == 1000
        assert data["energy"] == 500

# Тестирование сохранения в БД
def test_save_query_to_db():
    mock_tron_data = {
        "address": "TXYZ1234567890",
        "balance": 100.0,
        "bandwidth": 1000,
        "energy": 500,
    }

    db = SessionLocal()
    service = TronService()
    # Сохраняем данные в БД
    saved_query = service.save_query(**mock_tron_data)
    
    # Проверяем, что запись была сохранена
    assert saved_query.address == "TXYZ1234567890"
    assert saved_query.balance == 100.0
    assert saved_query.bandwidth == 1000
    assert saved_query.energy == 500

    # Очищаем БД после теста
    db.query(TronQuery).filter(TronQuery.address == "TXYZ1234567890").delete()
    db.commit()
    db.close()
