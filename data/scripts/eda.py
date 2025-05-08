import matplotlib.pyplot as plt

def plot_cases_and_deaths(df, country='Kenya'):
    """Plots total cases and deaths over time."""
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['total_cases'], label='Total Cases', color='blue')
    plt.plot(df['date'], df['total_deaths'], label='Total Deaths', color='red')
    plt.title(f"COVID-19 Total Cases and Deaths in {country}")
    plt.xlabel("Date")
    plt.ylabel("Count")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_daily_new_cases(df):
    """Plots new daily cases."""
    df = df[df['new_cases'] > 0]
    plt.figure(figsize=(12, 6))
    plt.bar(df['date'], df['new_cases'], color='orange')
    plt.title("Daily New COVID-19 Cases")
    plt.xlabel("Date")
    plt.ylabel("New Cases")
    plt.tight_layout()
    plt.show()
