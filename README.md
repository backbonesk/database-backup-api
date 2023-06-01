# database-backup-api

Database Backup Scheduler API

Built using python and fastapi

## Developing

Install dependencies using [poetry](https://python-poetry.org)

```
poetry install
```

Activate venv

```
poetry shell
```

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
