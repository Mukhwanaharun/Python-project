from scripts.load_data import load_covid_data
from scripts.clean_data import clean_data
from scripts.eda import plot_cases_and_deaths, plot_daily_new_cases
from scripts.vaccination_analysis import plot_vaccinations
from scripts.map_visualization import plot_choropleth

def main():
    FILEPATH = 'data/owid-covid-data.csv'

    df = load_covid_data(FILEPATH)
    if df is None:
        return

    kenya_df = clean_data(df, country='Kenya')

    # Exploratory Data Analysis
    plot_cases_and_deaths(kenya_df)
    plot_daily_new_cases(kenya_df)

    # Vaccination Analysis
    plot_vaccinations(kenya_df)

    # Choropleth Map
    plot_choropleth(df)
    print(df.head())

if __name__ == '_main_':
    main()
