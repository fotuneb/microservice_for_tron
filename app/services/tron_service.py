from tronpy import Tron
from tronpy.exceptions import AddressNotFound
from app.db.session import SessionLocal
from app.db.models import TronQuery
from datetime import datetime

class TronService:
    def __init__(self):
        self.client = Tron()

    def get_account_info(self, address: str):
        """Получает информацию о балансе, энергии и bandwidth по адресу"""
        try:
            account = self.client.get_account(address)
            balance = account.get("balance", 0) / 1_000_000  # Преобразуем в TRX
            bandwidth = self.client.get_account_resource(address).get("freeNetUsed", 0)
            energy = self.client.get_account_resource(address).get("energyUsed", 0)

            return {
                "address": address,
                "balance": balance,
                "bandwidth": bandwidth,
                "energy": energy,
            }
        except AddressNotFound as e:
            raise ValueError(f"Ошибка при получении данных из Tron: {e}")

    def save_query(self, address: str, balance: float, bandwidth: int, energy: int):
        """Сохраняет запрос в базу данных"""
        db = SessionLocal()
        try:
            query = TronQuery(
                address=address,
                balance=balance,
                bandwidth=bandwidth,
                energy=energy,
                timestamp=datetime.utcnow(),
            )
            db.add(query)
            db.commit()
            db.refresh(query)
            return query
        finally:
            db.close()