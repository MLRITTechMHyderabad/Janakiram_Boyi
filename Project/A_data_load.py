import pandas as pd

def load_data(data_path):
    try:
        df = pd.read_csv(data_path)
        print("Data Loaded Successfully!!!")
        print("\nPreview of the data:")
        print(df.head())
        return df
    except FileNotFoundError:
        print("File not Found. Please check the path.")
    except Exception as e:
        print(f"Error reading file: {e}")

