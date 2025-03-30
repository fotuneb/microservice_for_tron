# app/core/config.py
import os

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db/tron_db")

settings = Settings()
