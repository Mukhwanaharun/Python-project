import pandas as pd

def load_covid_data(filepath):
    """Loads the COVID-19 dataset."""
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully. Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        return df
    except Exception as e:
        print("Error loading data:", e)
        return None

