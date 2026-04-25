#Loads data from the silver file to duckdb
import duckdb

def load():
    conn = duckdb.connect("Data/pl_pipeline.db")
    conn.execute("CREATE TABLE IF NOT EXISTS TopScorers AS SELECT * FROM 'Data/Silver/topscorers_clean.parquet'")

    # Player with most goals
    bq1 = conn.execute("""
        SELECT name, team, goals 
        FROM TopScorers 
        ORDER BY goals DESC 
        LIMIT 1
    """).fetchdf()
    print("Most Goals:", bq1)
    print('\n')


    # Player with most assists
    bq2 = conn.execute("""
        SELECT name, team, assists 
        FROM TopScorers 
        ORDER BY assists DESC 
        LIMIT 1
    """).fetchdf()
    print("Most Assists:", bq2)
    print('\n')

    # Highest avg minutes per goal
    bq3 = conn.execute("""
        SELECT name, team, ROUND(minutes * 1.0 / goals, 2) AS mins_per_goal 
        FROM TopScorers 
        WHERE goals > 0
        ORDER BY mins_per_goal ASC 
        LIMIT 1
    """).fetchdf()
    print("Best mins per goal:", bq3)
    print('\n')

    # highest avg minutes per assist
    bq4 = conn.execute("""
        SELECT name, team, ROUND(minutes * 1.0 / assists, 2) AS mins_per_assist 
        FROM TopScorers 
        WHERE assists > 0
        ORDER BY mins_per_assist ASC 
        LIMIT 1
    """).fetchdf()
    print("Best mins per assist:", bq4)
    print('\n')


    result = conn.execute("SELECT * FROM TopScorers").fetchdf()
    result.to_csv("Data/topscorers.csv", index=False)
    print(result)