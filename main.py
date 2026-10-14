from ETL.extract import extract_data
from ETL.transform import transform_data
from ETL.load import load_data

def run():
    raw = extract_data()
    clean = transform_data(raw)
    load_data(clean)
    print(f"Loaded {len(clean)} rows")

if __name__ == "__main__":
    run()
