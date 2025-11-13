import sqlite3
import pandas as pd

db_path = r"C:\Users\tiffa\Desktop\Master\Oct25\smart-store-thildebrand\data\project.db"
conn = sqlite3.connect(db_path)

for table in ['customers_prepared', 'products_prepared', 'sales_prepared']:
    print(f"\nTable: {table}")
    df = pd.read_sql_query(f"SELECT * FROM {table} LIMIT 5;", conn)
    print(df.head())

conn.close()
