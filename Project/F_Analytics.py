import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt

def perform_analysis(df):
    top_countries = df['Country'].value_counts().head(30)
    print("\nTop Countries affected by Cyber Attacks are :\n", top_countries)

    print("\nThe Frequency of Different Attack Types are :")
    frequency = df['Attack_Types'].value_counts()
    print(frequency)

    print("\nYearly Trends in global CyberSecurity Incidents: ")
    yearly_trends = df['Year'].value_counts().sort_index()
    print(yearly_trends)

    print("\nSeverity levels and their impact by region: ")
    severity = df.groupby('Country')[['Financial_Loss_Million_USD', 'No_of_Affected_Users']].sum().sort_values(by='Financial_Loss_Million_USD', ascending=False).head(20)
    print(severity)

    print("\nCorrelation between attack type and sector targeted:")
    correlation = df.groupby(['Attack_Types', 'Target_Industries']).size().sort_values(ascending=False).head(20)
    print(correlation)

    top_loss = df.groupby('Country')['Financial_Loss_Million_USD'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    top_loss.plot(kind='barh', color='blue')
    plt.title('Top 10 Countries by Financial Loss (Million USD)')
    plt.xlabel('Financial Loss (Million USD)')
    plt.ylabel('Country')
    plt.tight_layout()
    plt.savefig("output_plot.png")
    