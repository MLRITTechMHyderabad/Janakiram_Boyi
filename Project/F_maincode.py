from A_data_load import load_data
from B_data_clean import clean_data
from E_my_sql_connect import insert_to_mysql
from C_Analytics import perform_analysis
from D_configure import DATA_PATH

def main():
    df = load_data(DATA_PATH)            
    df_cleaned = clean_data(df)          
    insert_to_mysql(df_cleaned)          
    perform_analysis(df_cleaned)          

if __name__ == "__main__":
    main()
