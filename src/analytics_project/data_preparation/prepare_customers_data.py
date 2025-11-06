"""
src/analytics_project/data_preparation/prepare_customers_data.py

This script reads customer data from the data/raw folder, cleans the data,
and writes the cleaned version to the data/prepared folder.

Tasks:
- Remove duplicates
- Handle missing values
- Standardize text formatting
"""

#####################################
# Import Modules
#####################################
import pathlib
import sys
import pandas as pd
import logging

# ------------------------------
# Project root & logger setup
# ------------------------------
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent.parent
sys.path.append(str(PROJECT_ROOT))

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

# ------------------------------
# File paths
# ------------------------------
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PREPARED_DATA_DIR = DATA_DIR / "prepared"

INPUT_FILE = RAW_DATA_DIR / "customers_data.csv"
OUTPUT_FILE = PREPARED_DATA_DIR / "customers_prepared.csv"

# ------------------------------
# Read & clean functions
# ------------------------------
def read_raw_data(file_path: pathlib.Path) -> pd.DataFrame:
    logger.info(f"Reading raw data: {file_path.name}")
    if not file_path.exists():
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"{file_path} does not exist")

    df = pd.read_csv(file_path)
    df.columns = [col.strip().lower() for col in df.columns]  # standardize column names
    logger.info(f"Loaded dataframe with {len(df)} rows and {len(df.columns)} columns")
    return df

def clean_customers_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting cleaning process...")

    # Remove duplicates
    initial_rows = len(df)
    df = df.drop_duplicates()
    logger.info(f"Removed duplicates: {initial_rows - len(df)} rows")

    # Handle missing values
    if "loyaltypoints" in df.columns:
        df["loyaltypoints"] = df["loyaltypoints"].fillna(0)
    if "preferredcontact" in df.columns:
        df["preferredcontact"] = df["preferredcontact"].fillna("unknown")

    # Standardize text formatting
    if "firstname" in df.columns:
        df["firstname"] = df["firstname"].str.strip().str.title()
    if "region" in df.columns:
        df["region"] = df["region"].str.strip().str.title()
    if "preferredcontact" in df.columns:
        df["preferredcontact"] = df["preferredcontact"].str.strip().str.lower()

    logger.info("Finished cleaning")
    return df

def save_prepared_data(df: pd.DataFrame, output_file: pathlib.Path):
    output_file.parent.mkdir(parents=True, exist_ok=True)  # ensure prepared folder exists
    df.to_csv(output_file, index=False)
    logger.info(f"Saved cleaned data to: {output_file}")

# ------------------------------
# Main
# ------------------------------
def main():
    logger.info("="*50)
    logger.info("STARTING prepare_customers_data.py")
    logger.info("="*50)

    df = read_raw_data(INPUT_FILE)
    df_clean = clean_customers_data(df)
    save_prepared_data(df_clean, OUTPUT_FILE)

    logger.info("="*50)
    logger.info("FINISHED prepare_customers_data.py")
    logger.info("="*50)

if __name__ == "__main__":
    main()
