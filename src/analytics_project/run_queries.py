import sqlite3
import pandas as pd
import os

# Paths
db_path = os.path.join(os.path.dirname(__file__), '../../data/project.db')
queries_path = os.path.join(os.path.dirname(__file__), 'SQL', 'queries.sql')

# Connect to database
conn = sqlite3.connect(db_path)

# Read SQL file
with open(queries_path, 'r') as f:
    sql_content = f.read()

# Split queries by semicolon
queries = [q.strip() for q in sql_content.split(';') if q.strip()]

# Run each query
for i, query in enumerate(queries, start=1):
    print(f"\n--- Query {i} ---")
    print(query)
    try:
        df = pd.read_sql_query(query, conn)
        print(df.head(10))  # Show first 10 rows
    except Exception as e:
        print("Error:", e)

conn.close()
print("\nAll queries executed.")
