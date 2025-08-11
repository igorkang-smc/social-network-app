# Social Network Application

A minimal Django project you can use as a starter: clean settings, sane defaults, and the usual dev tasks (run server, migrations, tests).

Steps:

* [x] Creating a login view
* [x] Using the Django authentication framework
* [x] Creating templates for Django login, logout, password change, and password reset views
* [x] Creating user registration views
* [x] Extending the user model with a custom profile model
* [x] Configuring the project for media file uploads


## Requirements
- Python 3.11+ (3.12 recommended)
- pip or uv / pipenv / poetry (pick your favorite)
- Git

---

## Quick Start

```bash
# 1) Virtual env
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 2) Install deps
pip install -U pip wheel
pip install -r requirements.txt  # or `pip install -e .` if using a pyproject

# 3) Environment variables
cp .env.example .env

# 4) DB + superuser
docker pull postgres:latest

docker run --name=social_db \
  -e POSTGRES_DB=social \
  -e POSTGRES_USER=social \
  -e POSTGRES_PASSWORD=xxxxx \
  -p 5432:5432 \
  -d postgres
  
cd mysite
python manage.py migrate
python manage.py createsuperuser

# 5) Run
python manage.py runserver
```
