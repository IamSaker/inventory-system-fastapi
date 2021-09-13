# Inventory System
A pure Python implementation of the inventory system using FastAPI, Docker, APScheduler, SQLAlchemy, PostgreSQL.

## File Structure
- `/app` - Python package in project
  - `__init__.py`
  - `app/crud`
  - `app/helpers`
  - `app/routes`
  - `main.py`
  - `config.py`
  - `db.py`
  - `models.py`
  - `schemas.py`
  - `requirements.txt`
- `/migrations`
  - `migrations/versions`
  - `env.py`
  - `script.py.mako`
- `/migrations`
- `.env`
- `alembic.ini`
- `Dockerfile`
- `docker-compose.yml`

## Tech Stack
- **FastAPI** - The API framework used.
- **APScheduler** - Python Scheduler.
- **SQLAlchemy** - Database ORM and models.
- **Alembic** - Database migrations.
- **PostgreSQL** - Object-relational database system.
- **Docker Compose** - Integration and optimization for local development.

## Development

Step 1 - `git clone repo`

Step 2 - `docker-compose up`
