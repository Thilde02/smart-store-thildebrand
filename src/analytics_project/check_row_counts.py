import pandas as pd
import os

# Folders containing the CSV files
raw_folder = r"C:\Users\tiffa\Desktop\Master\Oct25\smart-store-thildebrand\data\raw"
prepared_folder = r"C:\Users\tiffa\Desktop\Master\Oct25\smart-store-thildebrand\data\prepared"


# Function to count records in a folder
def count_records(folder):
    counts = {}
    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder, filename)
            try:
                df = pd.read_csv(file_path)
                counts[filename] = len(df)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
    return counts

# Count records
raw_counts = count_records(raw_folder)
prepared_counts = count_records(prepared_folder)

# Write counts to project.log
with open("project.log", "a") as log_file:
    log_file.write("=== Record Counts ===\n")

    log_file.write("Raw CSV Files:\n")
    for file, count in raw_counts.items():
        log_file.write(f"{file}: {count} records\n")

    log_file.write("\nPrepared CSV Files:\n")
    for file, count in prepared_counts.items():
        log_file.write(f"{file}: {count} records\n")

    log_file.write("\n====================\n\n")

print("Record counts logged to project.log!")

