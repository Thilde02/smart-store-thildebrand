import sqlite3

db_path = r"C:\Users\tiffa\Desktop\Master\Oct25\smart-store-thildebrand\data\project.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:", tables)

conn.close()
