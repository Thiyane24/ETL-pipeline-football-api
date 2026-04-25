# Premier League ETL Pipeline

An end-to-end data engineering pipeline that extracts Premier League top scorer data from the API-Football API, processes it through a medallion architecture, loads it into a local analytical warehouse, and visualises insights in Power BI.

---

## Architecture

![ETL Pipeline Architecture](API_pipeline_architecture.png)

---

## Tech Stack

| Layer | Tool |
|---|---|
| Data Source | API-Football v3 |
| Orchestration | Python |
| Storage | Apache Parquet |
| Warehouse | DuckDB |
| Containerisation | Docker |
| Visualisation | Power BI |

---

## Project Structure

```
ETL-pipeline-football-API/
├── Data/
│   ├── Bronze/        ← raw parquet files (with load ID timestamp)
│   └── Silver/        ← cleaned parquet files
├── Pipeline/
│   ├── extract.py     ← hits API, flattens JSON, saves to Bronze
│   ├── transform.py   ← cleans data, saves to Silver
│   └── load.py        ← loads to DuckDB, runs analytical queries
├── main.py            ← orchestrates the full pipeline
├── Dockerfile
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Pipeline Logic

### Extract
- Requests top scorer data from the Premier League 2024/25 season via API-Football
- Checks HTTP status code before processing
- Flattens nested JSON response into a tabular structure
- Saves raw data as Parquet to `Data/Bronze/` with a timestamp load ID

### Transform
- Reads the latest Parquet file from `Data/Bronze/`
- Renames columns for clarity (`id` → `player_id`)
- Casts data types to integers where appropriate
- Drops duplicate players
- Adds a `season` column
- Saves cleaned data to `Data/Silver/`

### Load
- Reads from `Data/Silver/`
- Loads data into a DuckDB analytical warehouse
- Runs 4 business queries against the warehouse

---

## Business Questions Answered

| # | Question |
|---|---|
| BQ1 | Which player scored the most goals? |
| BQ2 | Which player had the most assists? |
| BQ3 | Which player has the best average minutes per goal? |
| BQ4 | Which player has the best average minutes per assist? |

---

## Key Findings (2024/25 Season)

- **Most Goals** — Mohamed Salah (29 goals)
- **Most Assists** — Mohamed Salah (18 assists)
- **Best mins/goal** — Antoine Semenyo (most efficient scorer)
- **Best mins/assist** — Jean-Philippe Mateta (most efficient creator)

---

## How to Run

### Prerequisites
- Python 3.12+
- API key from [api-football.com](https://www.api-football.com)

### Setup

```bash
# Clone the repo
git clone https://github.com/Thiyane24/ETL-pipeline-football-API.git
cd ETL-pipeline-football-API

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your API key to .env
```

### Run the pipeline

```bash
python main.py
```

### Run with Docker

```bash
docker build -t pl-pipeline .
docker run --env-file .env pl-pipeline
```

---

## Environment Variables

Create a `.env` file based on `.env.example`:

```
API_KEY=your_api_football_key_here
```

---

## Notes

- This pipeline uses DuckDB as a local analytical warehouse, equivalent in query pattern to Google BigQuery (the intended production target)
- The free tier of API-Football allows 100 requests/day, sufficient for this pipeline which runs in a single call
- Power BI connects to the exported CSV from DuckDB for visualisation

---

## Dashboard Preview

4-page Power BI dashboard covering all business questions:
- Top scorers by goals
- Top scorers by assists
- Most efficient scorers (mins per goal)
- Most efficient creators (mins per assist)
