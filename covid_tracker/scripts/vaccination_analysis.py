import matplotlib.pyplot as plt

def plot_vaccinations(df):
    """Plots total vaccinations over time."""
    if 'total_vaccinations' not in df.columns:
        print("Vaccination data not available.")
        return
    df = df[df['total_vaccinations'] > 0]
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['total_vaccinations'], label='Total Vaccinations', color='green')
    plt.title("Vaccination Progress Over Time")
    plt.xlabel("Date")
    plt.ylabel("Total Vaccinations")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
