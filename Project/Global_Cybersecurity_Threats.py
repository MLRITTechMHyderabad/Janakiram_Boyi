
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import numpy as np
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt

# proper exception handling and file validation during the reading process
try:
    data_path = r"C:\Users\janak\Downloads\Global_Cybersecurity_Threats_2015-2024.csv"
    df = pd.read_csv(data_path)
    print("Data Loaded Successfully!!!")
    print("\nPreview of the data:")
    print(df.head())
    print()
    
    #Removing duplicates
    print("\nAfter Removing Duplicates:")
    df = df.drop_duplicates()
    print(df)
    
    #Handling missing values
    print("\nHandling Missing Values:")
    dfn = df.dropna()
    print(dfn)
    
    #Formatting inconsistent date format
    print("\nFormatting inconsistent date formats")
    df['Year'] =  pd.to_numeric(df['Year'], errors = 'coerce')
    df = df.dropna(subset=['Year'])
    df['Year'] = df['Year'].astype(int)
    
	#Formatting inconsistent region formats
    print("\nFormatting inconsistent region formats:")
    df['Country'] = df['Country'].str.strip().str.title()
    print(df['Country'].unique())
    
    #Normalizing categorical fields
    print("\n Normalizing categorical Fields:")
    df['Country'] = df['Country'].str.strip().str.title()
    df['Attack Type'] = df['Attack Type'].str.strip().str.title()
    df['Target Industry'] = df['Target Industry'].str.strip().str.title()
    df['Attack Source'] = df['Attack Source'].str.strip().str.title()
    df['Security Vulnerability Type'] = df['Security Vulnerability Type'].str.strip().str.title()
    df['Defense Mechanism Used'] = df['Defense Mechanism Used'].str.strip().str.title()
    
    #Renaming columns for clarity
    print("\nRenaming columns for clarity:")
    df = df.rename(columns = { 
        'Target Industry' : 'Target_Industries',
        'Attack Type' : 'Attack_Types',
        'Defense Mechanism Used' : 'Defense_Mechanisms',
        'Security Vulnerability Type': 'Vulnerability_Types',
        'Incident Resolution Time (in Hours)' : 'Incident_resolution_Time_Hrs',
        'Financial Loss (in Million $)': 'Financial_Loss_Million_USD',
        'Attack Source' : 'Attack_Source',
        'Number of Affected Users' : 'No_of_Affected_Users'   
    })
    
    print(df) 
except FileNotFoundError:
    print("File not Found. Please check the path.")
    
except Exception as e:
    print(f"Error reading file : {e}")

################################### MySQL Integration ###################################################
conn = mysql.connector.connect(
    host ='localhost', 
    user = 'root',
    password = 'root'
    )

cursor = conn.cursor()
#Creating database 
cursor.execute("CREATE DATABASE IF NOT EXISTS CyberSecurity; ")
conn.commit
cursor.close()
conn.close()

conn = mysql.connector.connect(
    host ='localhost', 
    user = 'root',
    password = 'root', 
    database = 'CyberSecurity'
    )

cursor = conn.cursor()

cursor.execute('''Create table IF NOT EXISTS ThreatAnalysis(Country VARCHAR(100), Year INT, Attack_Types VARCHAR(100), 
                Target_Industries VARCHAR(100), Financial_Loss_Million_USD FLOAT, No_of_Affected_Users INT,Attack_Source VARCHAR(100),
                Vulnerability_Types VARCHAR(100),  Defense_Mechanisms VARCHAR(100),  Incident_resolution_Time_Hrs Float)
                ''')
engine = create_engine("mysql+mysqlconnector://root:root@localhost/CyberSecurity")
df.to_sql (name = "ThreatAnalysis", con = engine, if_exists = "append", index = False)

print("Data has been Inserted Successfully into the MySQL Database!!")
conn.commit()

################################## Analytical Computation ############################################

#Top countries affected by cyber attacks
top_countries = df['Country'].value_counts().head(30)
print("\nTop Countries affected by Cyber Attacks are :\n",top_countries)

#Frequency of different types of threats (e.g., phishing, malware, ransomware)
print("\nThe Frequency of Different Attack Types are :")
Frequency = df['Attack_Types'].value_counts()
print(Frequency)

#Year-over-year trends in global cybersecurity incidents
print("\nYearly Trends in global CyberSecurity Incidents: ")
yearly_trends = df['Year'].value_counts().sort_index()
print(yearly_trends)

#Severity levels and their impact by region
print("\nSeverity levels and their impact by region: ")
Severity = df.groupby('Country')[['Financial_Loss_Million_USD', 'No_of_Affected_Users']].sum().sort_values(by = 'Financial_Loss_Million_USD', ascending = False).head(20)
print(Severity)

# Correlation between attack type and sector targeted
print("\nCorrelation between attack type and sector targeted:")
Correlation = df.groupby(['Attack_Types', 'Target_Industries']).size().sort_values(ascending=False).head(20)
print(Correlation)

####################################### Console Output ##################################################
#Summary statistics
print("\n******** Summary Statistics ********")
print(df.describe(include="all").transpose())

#Most frequent threat types
print("\n******** Most Frequent Threat Types ********")
print(df['Attack_Types'].value_counts().head(20))

#Region-wise or year-wise breakdowns
print("\n******** Region-wise or year-wise breakdowns ********")
print(df['Country'].value_counts().head(20))


#Key trends and outliers in the dataset
print("\n******** Key trends and outliers in the dataset ********")

print("\n-------- Top Incidents with Highest Loss --------")
print(df[['Country', 'Attack_Types', 'Financial_Loss_Million_USD']].sort_values(by= 'Financial_Loss_Million_USD', ascending = False).head(10).reset_index(drop=True))

print("\n-------- Top Incidents with Most Affected Users --------")
print(df[['Country','Attack_Types','No_of_Affected_Users']].sort_values(by = 'No_of_Affected_Users', ascending = False).head(10).reset_index(drop = True))


print("\n-------- Top loss with Most Affected Users --------")
top_loss = df.groupby('Country')['Financial_Loss_Million_USD'] .sum().sort_values(ascending=False).head(10)
print(top_loss)

# Plotting Top 10 Countries with the Highest Financial Loss
top_loss = df.groupby('Country')['Financial_Loss_Million_USD'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
top_loss.plot(kind='barh', color='blue')
plt.title('Top 10 Countries by Financial Loss (Million USD)')
plt.xlabel('Financial Loss (Million USD)')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig("output_plot.png")  # Saves the plot as an image
plt.show()
