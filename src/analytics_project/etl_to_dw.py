import sqlite3
import pandas as pd
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

PREPARED_DATA_DIR = BASE_DIR / "data" / "prepared"

# 🔥 UPDATED: Use project.db instead of smart_store_dw.sqlite
DB_PATH = BASE_DIR / "data" / "smart_sales.db"


# ---------------------------------------------------------------------------
# Load CSVs
# ---------------------------------------------------------------------------
def load_prepared_data():
    try:
        print("📥 Loading: customers_prepared.csv")
        customers = pd.read_csv(PREPARED_DATA_DIR / "customers_prepared.csv")

        print("📥 Loading: products_prepared.csv")
        products = pd.read_csv(PREPARED_DATA_DIR / "products_prepared.csv")

        print("📥 Loading: sales_prepared.csv")
        sales = pd.read_csv(PREPARED_DATA_DIR / "sales_prepared.csv")

        return customers, products, sales

    except Exception as e:
        print(f"❌ Error loading CSVs: {e}")
        raise


# ---------------------------------------------------------------------------
# Insert Data into SQLite
# ---------------------------------------------------------------------------
def load_data_to_db():
    print("🚀 Starting ETL to Data Warehouse")

    customers_df, products_df, sales_df = load_prepared_data()

    conn = None
    try:
        print(f"🔗 Connecting to DB at: {DB_PATH}")
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # --------------------------
        # Insert Customers
        # --------------------------
        print("➡️ Inserting customers...")
        customers_df.to_sql("dim_customer", conn, if_exists="append", index=False)

        # --------------------------
        # Insert Products
        # --------------------------
        print("➡️ Inserting products...")
        products_df.to_sql("dim_product", conn, if_exists="append", index=False)

        # --------------------------
        # Insert Sales (Fact Table)
        # --------------------------
        print("➡️ Inserting sales...")
        sales_df.to_sql("fact_sales", conn, if_exists="append", index=False)

        conn.commit()
        print("✅ ETL process completed successfully!")

    except Exception as e:
        print(f"❌ Error during ETL: {e}")

    finally:
        if conn:
            conn.close()
            print("🔒 Database connection closed.")


# ---------------------------------------------------------------------------
# Run ETL
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    load_data_to_db()

