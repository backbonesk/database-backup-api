# database-backup-api

Database Backup Scheduler API

Built using python and fastapi

## Setup

Install dependencies using [poetry](https://python-poetry.org)

```bash
poetry install
```

Activate venv

```bash
poetry shell
```

## Database

Enter `psql`

```bash
psql
```

Create database

```sql
CREATE DATABASE database_backup;
```

Create migrations

```bash
alembic revision --autogenerate -m "init"
```

Apply migrations

```bash
alembic upgrade head
```

## Developing

Run dev server (creates postgres tables)

```
uvicorn app.main:app --reload
```

## Testing

Restore pg dump sql file

```
psql -d dbname -f backupdest.sql
```

Open http://127.0.0.1:8000 in your browser.
