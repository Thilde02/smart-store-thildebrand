import pandas as pd
from pathlib import Path

# ===============================
# Define directories and folders
# ===============================
# Go up two levels from src/analytics_project to reach the project root
BASE_DIR = Path(__file__).resolve().parents[2]

# Define correct input (raw) and output (prepared) directories
RAW_DIR = BASE_DIR / "data" / "raw"
PREPARED_DIR = BASE_DIR / "data" / "prepared"

# Create the prepared directory if it doesn't exist
PREPARED_DIR.mkdir(parents=True, exist_ok=True)

# ===============================
# Define cleaning function
# ===============================
def clean_dataframe(df):
    """Perform basic data cleaning steps on a pandas DataFrame."""

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values with 'Unknown'
    df = df.fillna("Unknown")

    # Convert all column names to lowercase, remove spaces, and strip whitespace
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Ensure all string values are stripped of whitespace
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.strip()

    return df

# ===============================
# Define processing function
# ===============================
def process_and_save(filename, output_name):
    """Read a CSV file, clean it, and save to the prepared folder."""
    input_path = RAW_DIR / filename
    output_path = PREPARED_DIR / output_name

    if not input_path.exists():
        print(f"⚠️ File not found: {input_path}")
        return

    print(f"Processing {filename}...")

    # Read, clean, and save
    df = pd.read_csv(input_path)
    cleaned_df = clean_dataframe(df)
    cleaned_df.to_csv(output_path, index=False)

    print(f"✅ Saved cleaned data to: {output_path}")

# ===============================
# Process all raw data files
# ===============================
process_and_save("customers_data.csv", "customers_prepared.csv")
process_and_save("products_data.csv", "products_prepared.csv")
process_and_save("sales_data.csv", "sales_prepared.csv")

print("🎉 All files processed and saved successfully!")
