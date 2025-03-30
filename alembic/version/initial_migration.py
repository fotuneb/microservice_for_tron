alembic revision --autogenerate -m "initial migration"
alembic upgrade head
alembic downgrade base