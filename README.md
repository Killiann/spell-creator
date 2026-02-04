# spell-creator-backend

Running seed from venv: ENV_FILE=.env.local python -m app.seed.seed_all

Run frontend dev: 
cd frontend
npm run dev

Alembic:
revision:
ENV_FILE=.env.local alembic revision --autogenerate -m "Make spell name unique"

upgrade head:

ENV_FILE=.env.local alembic upgrade head