import pandas as pd

def clean_data(df, country='Kenya'):
    """Cleans and filters data for a specific country."""
    df = df[df['location'] == country]
    df = df.dropna(subset=['date', 'total_cases', 'total_deaths'])
    df['date'] = pd.to_datetime(df['date'])
    df = df.fillna(0)
    return df