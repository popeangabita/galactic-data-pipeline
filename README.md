# Cosmic Catalog

Some **data engineering project** that I thought sounds cool which builds a small **space data warehouse** (if you want to call it like that) using real astronomical datasets.
The pipeline extracts public data about **exoplanets**, **near-Earth asteroids**, and **stars**, loads them into **PostgreSQL**, transforms them using Python, and creates **mart views** for exploration.

---

## Project Overview

This project demonstrates practical DE concepts using a fully free and open-source stack:

- **Python** (Pandas, Requests, SQLAlchemy)  
- **PostgreSQL** (local)  
- **Raw → Curated → Mart** warehouse structure  
- **Automated pipeline script** (PowerShell; Airflow optional for future)

The warehouse lets you answer questions such as:

- Which exoplanets might be **habitable**?  
- Which asteroids will pass **closest** to Earth in the near future?  
- Which nearby stars are **brightest** or **closest** to Earth?

---

## Data Sources

### 1. NASA Exoplanet Archive – Exoplanet Properties  
https://exoplanetarchive.ipac.caltech.edu  

Used for the planet dimension (`dim_planet`).  
Includes:
- planet radius
- orbital period
- equilibrium temperature
- host star distance
- discovery year
- discovery method

### 2. JPL SBDB – Near-Earth Object Close Approaches  
https://ssd.jpl.nasa.gov/tools/ca/  

Used for `fact_close_approach`.  
Includes:
- asteroid designation
- close-approach date & distance (AU)
- relative velocity
- orbit ID

### 3. HYG Star Catalog (Hipparcos–Yale–Gliese)  
https://github.com/astronexus/HYG-Database  

Used for `dim_star`.  
Includes:
- HIP identifier
- star name
- magnitude
- distance (parsecs)
- spectral type

## Installation & Setup
*In case you want to play with it, you know? :)*

### 1. Clone the repository
```bash
git clone https://github.com/popeangabita/galactic-data-pipeline.git
cd galactic-data-pipeline
```

### 2. Create a virtual environment
```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell**
```powershell
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Add environment variables
Create a file named `.env`:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=cosmic_catalog
DB_USER=<your-postgres-username>
DB_PASS=<your-postgres-password>

POSTGRES_URL=postgresql+psycopg2://<your-postgres-username>:<your-postgres-password>@localhost:5432/cosmic_catalog
POSTGRES_ADMIN=postgresql+psycopg2://<your-postgres-username>:<your-postgres-password>@localhost:5432/postgres
```

Replace `<your-postgres-username>` and `<your-postgres-password>` with your local PostgreSQL credentials.

### 6. Run the pipeline
```powershell
.\run_pipeline.ps1
```
