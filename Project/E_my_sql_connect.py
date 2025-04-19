import mysql.connector
from sqlalchemy import create_engine
from D_configure import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB

def insert_to_mysql(df):
    try:

        conn = mysql.connector.connect(
            host=MYSQL_HOST, 
            user=MYSQL_USER, 
            password=MYSQL_PASSWORD
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {MYSQL_DB};")
        conn.commit()

        conn = mysql.connector.connect(
            host=MYSQL_HOST, 
            user=MYSQL_USER, 
            password=MYSQL_PASSWORD, 
            database=MYSQL_DB
        )
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS ThreatAnalysis(
            Country VARCHAR(100), 
            Year INT, 
            Attack_Types VARCHAR(100), 
            Target_Industries VARCHAR(100), 
            Financial_Loss_Million_USD FLOAT, 
            No_of_Affected_Users INT, 
            Attack_Source VARCHAR(100), 
            Vulnerability_Types VARCHAR(100), 
            Defense_Mechanisms VARCHAR(100), 
            Incident_resolution_Time_Hrs FLOAT)''')

        engine = create_engine(f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}")
        df.to_sql(name="ThreatAnalysis", con=engine, if_exists="append", index=False)

        print("Data has been inserted successfully into the MySQL Database!")

    except Exception as e:
        print(f"Error inserting data to MySQL: {e}")
