"""
scripts/data_preparation/prepare_products.py

This script reads data from the data/raw folder, cleans the data,
and writes the cleaned version to the data/prepared folder.

Tasks:
- Remove duplicates
- Handle missing values
- Remove outliers
- Ensure consistent formatting

"""

######################################
# Import Modules
#####################################
import pathlib
import sys
import pandas as pd

# Add parent folder to sys.path
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

from utils_logger import logger

SCRIPTS_DATA_PREP_DIR = pathlib.Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPTS_DATA_PREP_DIR.parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PREPARED_DATA_DIR = DATA_DIR / "prepared"

RAW_DATA_DIR.mkdir(exist_ok=True)
PREPARED_DATA_DIR.mkdir(exist_ok=True)


def read_raw_data(file_name: str) -> pd.DataFrame:
    logger.info(f"Reading raw data: {file_name}")
    df = pd.read_csv(RAW_DATA_DIR / file_name)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "")
    logger.info(f"Loaded dataframe with {len(df)} rows and {len(df.columns)} columns")
    return df


def clean_products_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting cleaning process...")

    # Remove duplicates
    before = len(df)
    df = df.drop_duplicates()
    logger.info(f"Removed duplicates: {before - len(df)} rows")

    # Handle missing values
    for col in ["price", "stockquantity"]:  # numeric example
        if col in df.columns:
            df[col] = df[col].fillna(df[col].median())
    for col in ["category", "brand"]:  # categorical example
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")
    logger.info("Handled missing values")

    # Remove impossible numeric values
    if "price" in df.columns:
        df = df[df["price"] >= 0]
    if "stockquantity" in df.columns:
        df = df[df["stockquantity"] >= 0]

    logger.info("Finished cleaning")
    return df


def main():
    logger.info("==================================")
    logger.info("STARTING prepare_products_data.py")
    logger.info("==================================")

    df = read_raw_data("products_data.csv")
    df_clean = clean_products_data(df)

    output_file = PREPARED_DATA_DIR / "products_prepared.csv"
    df_clean.to_csv(output_file, index=False)
    logger.info(f"Saved cleaned data to: {output_file}")

    logger.info("FINISHED prepare_products_data.py")
    logger.info("==================================")


if __name__ == "__main__":
    main()

