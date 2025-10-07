# Demo Database

A Flask web application for database demonstrations.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and go to `http://localhost:5000`

## Project Structure

```
DemoDatabase/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   └── index.html
└── static/             # Static files (CSS, JS, images)
```

## Configuration

This project supports environment-based configuration. Use the provided `config.py` and a `.env` file to customize settings.

- Copy the example file and edit values:

```bash
cp .env.example .env
# then edit .env and set your SECRET_KEY and DATABASE_URL
```

- `config.py` provides `Config`, `DevelopmentConfig`, and `ProductionConfig` classes. Example usage in `app.py`:

```python
from config import DevelopmentConfig
app.config.from_object(DevelopmentConfig)
```

The `SECRET_KEY` and `DATABASE_URL` will be read from environment variables if set; otherwise defaults from `.env` will be used when you load them into the environment.

To load `.env` automatically you can install `python-dotenv` and add at the top of `app.py`:

```python
from dotenv import load_dotenv
load_dotenv()
```

### SQL Server (MSSQL) support

The `config.py` can construct a SQL Server URI when you provide MSSQL-related environment variables. You can either set a full `DATABASE_URL` (preferred), or provide the individual parts:

Environment variables supported:

- `MSSQL_HOST` (e.g. `db.example.com`)
- `MSSQL_PORT` (optional, e.g. `1433`)
- `MSSQL_USER`
- `MSSQL_PASSWORD`
- `MSSQL_DATABASE`
- `MSSQL_DRIVER` (optional, default: `ODBC Driver 18 for SQL Server`)

Example `.env` entries:

```
MSSQL_HOST=127.0.0.1
MSSQL_PORT=1433
MSSQL_USER=myuser
MSSQL_PASSWORD=secret
MSSQL_DATABASE=mydb
MSSQL_DRIVER=ODBC Driver 18 for SQL Server
```

Note: The config currently builds a SQLAlchemy URL for `pyodbc` (e.g. `mssql+pyodbc://user:pass@host:port/db?driver=ODBC+Driver+18+for+SQL+Server`). Make sure you have the appropriate ODBC driver installed on your machine and `pyodbc` in `requirements.txt` if you want to use this driver.
