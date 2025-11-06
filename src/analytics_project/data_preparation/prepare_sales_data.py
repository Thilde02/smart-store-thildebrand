"""
scripts/data_preparation/prepare_sales.py

This script reads data from the data/raw folder, cleans the data,
and writes the cleaned version to the data/prepared folder.

Tasks:
- Remove duplicates
- Handle missing values
- Remove outliers
- Ensure consistent formatting

"""

#####################################
# Import Modules
#####################################
import pathlib
import sys
import pandas as pd

# Add parent folder to sys.path
sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent))

from utils_logger import logger

#####################################
# Constants
#####################################
SCRIPTS_DATA_PREP_DIR = pathlib.Path(__file__).resolve().parent
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PREPARED_DATA_DIR = DATA_DIR / "prepared"

# Ensure directories exist
RAW_DATA_DIR.mkdir(exist_ok=True)
PREPARED_DATA_DIR.mkdir(exist_ok=True)

#####################################
# Functions
#####################################

def read_raw_data(file_name: str) -> pd.DataFrame:
    """Read raw CSV data into a DataFrame"""
    logger.info(f"Reading raw data: {file_name}")
    file_path = RAW_DATA_DIR / file_name
    df = pd.read_csv(file_path)

    # Standardize column names: lowercase, strip spaces, no underscores
    df.columns = df.columns.str.strip().str.lower()

    logger.info(f"Columns after standardizing: {df.columns.tolist()}")
    logger.info(f"Loaded dataframe with {len(df)} rows and {len(df.columns)} columns")
    return df

def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the sales DataFrame"""
    logger.info("Starting cleaning process...")

    # Remove duplicate rows
    initial_rows = len(df)
    df = df.drop_duplicates()
    removed_duplicates = initial_rows - len(df)
    logger.info(f"Removed duplicates: {removed_duplicates} rows")

    # Handle missing values
    df.loc[:, 'saleamount'] = df['saleamount'].fillna(df['saleamount'].median())
    df.loc[:, 'discountpercent'] = df['discountpercent'].fillna(0)
    logger.info("Handled missing values for saleamount and discountpercent")

    # Remove negative sale amounts
    initial_rows = len(df)
    df = df[df['saleamount'] >= 0]
    removed_negatives = initial_rows - len(df)
    logger.info(f"Removed negative saleamount: {removed_negatives} rows")

    # Fix text formatting in paymenttype
    df.loc[:, 'paymenttype'] = df['paymenttype'].astype(str).str.strip().str.title()
    logger.info("Cleaned paymenttype column formatting")

    return df

def save_prepared_data(df: pd.DataFrame, file_name: str) -> None:
    """Save cleaned DataFrame to prepared folder"""
    output_path = PREPARED_DATA_DIR / file_name
    df.to_csv(output_path, index=False)
    logger.info(f"Saved cleaned data to {output_path}")

#####################################
# Main Execution
#####################################

def main():
    logger.info("==================================")
    logger.info("STARTING prepare_sales_data.py")
    logger.info("==================================")

    input_file = "sales_data.csv"
    output_file = "sales_prepared.csv"

    df = read_raw_data(input_file)
    df_clean = clean_sales_data(df)
    save_prepared_data(df_clean, output_file)

    logger.info("==================================")
    logger.info("FINISHED prepare_sales_data.py")
    logger.info("==================================")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()
