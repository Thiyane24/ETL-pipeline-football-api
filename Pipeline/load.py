import duckdb

def load():
  conn = duckdb.connect("Data/pl_pipeline.db")
  conn.execute("CREATE TABLE IF NOT EXISTS TopScorers AS SELECT * FROM 'Data/Silver/topscorers_clean.parquet'")

  result = conn.execute("SELECT * FROM TopScorers").fetchdf()

  print(result)