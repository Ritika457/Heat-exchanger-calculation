# Heat Exchanger Cleaning Optimizer

A full-stack engineering application for monitoring heat-exchanger operating data, calculating thermal-performance indicators, and retaining calculation history. The project combines a FastAPI backend, a browser-based dashboard, and Microsoft SQL Server integration.

## What it does

- Calculates shell-side and tube-side heat duty
- Calculates LMTD and corrected LMTD
- Computes the correction factor and overall heat-transfer coefficients
- Reads the latest process-tag values from SQL Server
- Stores and displays calculation history
- Provides an interactive web dashboard and API documentation

## Technology

- **Backend:** Python, FastAPI, Pydantic
- **Data and calculations:** NumPy, Pandas, SciPy
- **Database:** Microsoft SQL Server through `pyodbc`
- **Frontend:** HTML, CSS, and JavaScript

## Project structure

```text
heat_exchanger/
├── backend/
│   ├── app/
│   │   ├── calculations/    # Thermal calculation functions
│   │   ├── database/        # Database configuration and connection
│   │   ├── models/          # Request and response models
│   │   ├── repositories/    # Data persistence
│   │   ├── routers/         # API endpoints
│   │   ├── services/        # Application workflow
│   │   └── main.py          # FastAPI application
│   └── tests/               # Unit tests
├── frontend/                # Dashboard, styles, and browser logic
├── .env.example             # Safe configuration template
└── requirements.txt         # Python dependencies
```

## Local setup

### 1. Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The checked-in project intentionally excludes local virtual environments.

### 2. Configure the database

Copy `.env.example` to `backend/.env`, then provide your own SQL Server settings and dashboard credentials:

```powershell
Copy-Item .env.example backend\.env
```

The application expects the following tables:

- `HeatExchangerCalculation` for saved calculation results
- `Heat_Exchanger_Taglist` for live values with `Name`, `Value`, and `Time` columns

Install **Microsoft ODBC Driver 17 for SQL Server** on the machine running the backend. Real credentials and operational datasets must remain local and must not be committed.

### 3. Run the application

```powershell
Set-Location backend
python -m uvicorn app.main:app --reload
```

Open:

- Dashboard: <http://127.0.0.1:8000>
- Interactive API documentation: <http://127.0.0.1:8000/docs>
- Health check: <http://127.0.0.1:8000/api/health>

## Run the tests

From the `backend` directory:

```powershell
python -m unittest discover -s tests -v
```

## API overview

| Method | Endpoint | Purpose |
| --- | --- | --- |
| `GET` | `/api/health` | Confirm that the backend is running |
| `POST` | `/api/login` | Validate dashboard access |
| `POST` | `/api/calculate` | Calculate and store exchanger performance |
| `GET` | `/api/history` | Retrieve previous calculations |
| `GET` | `/api/live-tags` | Retrieve the latest process-tag values |

## Security and data privacy

- Database secrets are loaded from `backend/.env`, which is ignored by Git.
- Spreadsheet data, database exports, logs, and local environments are excluded from the repository.
- Use synthetic or anonymized data for screenshots and demonstrations.
- Dashboard credentials are read from the local environment instead of being embedded in source code.
- The current login remains a demonstration feature, not production authentication.

## Future improvements

- Replace the demonstration login with secure authentication
- Add database migrations and a reproducible schema
- Add input-domain validation for thermal calculations
- Add automated API and browser tests
- Containerize the application for deployment

## Disclaimer

This project is intended as an engineering and software-development demonstration. Calculation results should be independently validated before use in operational or safety-critical decisions.
