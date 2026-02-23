# ---------- Builder ----------
FROM python:3.13-slim AS builder

ENV POETRY_VERSION=2.0.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir poetry==$POETRY_VERSION

COPY pyproject.toml poetry.lock* ./

RUN poetry install --only main --no-root

COPY app ./app


# ---------- Runtime ----------
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY --from=builder /app/app ./app

EXPOSE 8000

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "-b", "0.0.0.0:8000", "app.main:app"]