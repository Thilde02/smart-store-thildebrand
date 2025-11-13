import sqlite3
import pandas as pd
import os

# Paths
data_folder = os.path.join(os.path.dirname(__file__), '../../data/prepared')
db_path = os.path.join(os.path.dirname(__file__), '../../data/project.db')

# Debug: check folder and files
print("Looking for CSVs in:", data_folder)
print("Files found:", os.listdir(data_folder))

# SQLite reserved keywords (partial)
sqlite_keywords = {
    "ABORT","ACTION","ADD","AFTER","ALL","ALTER","ANALYZE","AND","AS","ASC","ATTACH",
    "AUTOINCREMENT","BEFORE","BEGIN","BETWEEN","BY","CASCADE","CASE","CAST","CHECK",
    "COLLATE","COLUMN","COMMIT","CONFLICT","CONSTRAINT","CREATE","CROSS","CURRENT_DATE",
    "CURRENT_TIME","CURRENT_TIMESTAMP","DATABASE","DEFAULT","DEFERRABLE","DEFERRED",
    "DELETE","DESC","DETACH","DISTINCT","DROP","EACH","ELSE","END","ESCAPE","EXCEPT",
    "EXCLUSIVE","EXISTS","EXPLAIN","FAIL","FOR","FOREIGN","FROM","FULL","GLOB","GROUP",
    "HAVING","IF","IGNORE","IMMEDIATE","IN","INDEX","INDEXED","INITIALLY","INNER","INSERT",
    "INSTEAD","INTERSECT","INTO","IS","ISNULL","JOIN","KEY","LEFT","LIKE","LIMIT","MATCH",
    "NATURAL","NO","NOT","NOTNULL","NULL","OF","OFFSET","ON","OR","ORDER","OUTER","PLAN",
    "PRAGMA","PRIMARY","QUERY","RAISE","RECURSIVE","REFERENCES","REGEXP","REINDEX","RELEASE",
    "RENAME","REPLACE","RESTRICT","RIGHT","ROLLBACK","ROW","SAVEPOINT","SELECT","SET","TABLE",
    "TEMP","TEMPORARY","THEN","TO","TRANSACTION","TRIGGER","UNION","UNIQUE","UPDATE","USING",
    "VACUUM","VALUES","VIEW","VIRTUAL","WHEN","WHERE","WITH","WITHOUT"
}

# Connect to SQLite (will create new project.db)
conn = sqlite3.connect(db_path)

# List CSV files
csv_files = [f for f in os.listdir(data_folder) if f.lower().endswith('.csv')]
if not csv_files:
    print("No CSV files found in", data_folder)
else:
    for filename in csv_files:
        table_name = os.path.splitext(filename)[0]
        csv_path = os.path.join(data_folder, filename)
        df = pd.read_csv(csv_path)

        # Sanitize column names
        new_columns = []
        for c in df.columns:
            col = c.strip().replace(' ', '_').replace('.', '_').replace('"','').replace("'",'')
            if col.upper() in sqlite_keywords:
                col = col + "_col"
            new_columns.append(col)
        df.columns = new_columns

        # Import into SQLite
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"Imported {filename} into table {table_name}")

conn.close()
print("Database created successfully at:", db_path)

