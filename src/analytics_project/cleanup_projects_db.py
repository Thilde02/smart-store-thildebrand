import sqlite3
from pathlib import Path

db_path = Path(r"C:\Users\tiffa\Desktop\Master\Oct25\smart-store-thildebrand\data\project.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

tables_to_delete = ["dim_customer", "dim_product", "fact_sales"]
for table in tables_to_delete:
    cursor.execute(f"DROP TABLE IF EXISTS {table}")
    print(f"Dropped {table}")

conn.commit()
conn.close()
print("All selected tables deleted from project.db")
