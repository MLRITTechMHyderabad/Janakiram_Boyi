from data_load import load_data
from data_clean import clean_data
from my_sql_connect import insert_to_mysql
from Analytics import perform_analysis
from configure import DATA_PATH

def main():
    df = load_data(DATA_PATH)
    df_cleaned = clean_data(df)
    insert_to_mysql(df_cleaned)
    perform_analysis(df_cleaned)

if __name__ == "__main__":
    main()
