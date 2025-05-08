import plotly.express as px
import pandas as pd

def plot_choropleth(df):
    """Plots a choropleth map of total cases per country."""
    latest_date = df['date'].max()
    latest_df = df[df['date'] == latest_date]
    map_df = latest_df[['iso_code', 'location', 'total_cases']].dropna()

    fig = px.choropleth(
        map_df,
        locations="iso_code",
        color="total_cases",
        hover_name="location",
        color_continuous_scale="Reds",
        title=f"Global COVID-19 Cases as of {latest_date.date()}"
    )
    fig.show()

