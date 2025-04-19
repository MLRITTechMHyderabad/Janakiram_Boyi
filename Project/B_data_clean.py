import pandas as pd

def clean_data(df):
    print("\nAfter Removing Duplicates:")
    df = df.drop_duplicates()
    print(df)

    print("\nHandling Missing Values:")
    dfn = df.dropna()
    print(dfn)

    print("\nFormatting inconsistent date formats")
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df = df.dropna(subset=['Year'])
    df['Year'] = df['Year'].astype(int)

    print("\nFormatting inconsistent region formats:")
    df['Country'] = df['Country'].str.strip().str.title()
    print(df['Country'].unique())

    print("\n Normalizing categorical Fields:")
    df['Country'] = df['Country'].str.strip().str.title()
    df['Attack Type'] = df['Attack Type'].str.strip().str.title()
    df['Target Industry'] = df['Target Industry'].str.strip().str.title()
    df['Attack Source'] = df['Attack Source'].str.strip().str.title()
    df['Security Vulnerability Type'] = df['Security Vulnerability Type'].str.strip().str.title()
    df['Defense Mechanism Used'] = df['Defense Mechanism Used'].str.strip().str.title()

    print("\nRenaming columns for clarity:")
    df = df.rename(columns={ 
        'Target Industry': 'Target_Industries',
        'Attack Type': 'Attack_Types',
        'Defense Mechanism Used': 'Defense_Mechanisms',
        'Security Vulnerability Type': 'Vulnerability_Types',
        'Incident Resolution Time (in Hours)': 'Incident_resolution_Time_Hrs',
        'Financial Loss (in Million $)': 'Financial_Loss_Million_USD',
        'Attack Source': 'Attack_Source',
        'Number of Affected Users': 'No_of_Affected_Users'   
    })
    
    return df
