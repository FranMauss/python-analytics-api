# Python Analytics API

REST API built with FastAPI to analyze sales data using PostgreSQL and Python.

## Tech Stack
- Python 3.10
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pandas

## Setup
1. Create virtual environment:
python -m venv venv

2. Activate venv:

venv\Scripts\Activate.ps1

3. Install requirements:

pip install -r requirements.txt

4. Run server:

uvicorn app.main:app --reload

5. Run db

python -m app.init_db