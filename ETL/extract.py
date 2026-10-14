import csv

def extract_data(path="data/input.csv"):
    rows = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            rows.append(row)
    return rows
# Extract step: reads the input CSV
# Rows are read as dictionaries
