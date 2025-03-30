from sqlalchemy import Column, Integer, String, Float, DateTime
from .session import Base
from datetime import datetime

class TronQuery(Base):
    __tablename__ = "tron_queries"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True, nullable=False)
    balance = Column(Float, nullable=False)
    bandwidth = Column(Integer, nullable=False)
    energy = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)