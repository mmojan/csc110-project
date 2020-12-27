"""CSC110 Fall 2020 Project: Cleaning the Data

Instructions
===============================

This Python module contains several functions that perform computations on
dataframes or create new dataframes for our use in the other modules of
this project.

Copyright Information
===============================

This file is Copyright (c) 2020 Mojan Majid, Kimiya Raminrad, Dorsa Molaverdikhani, Ayesha Nasir.
"""
import math
import pandas as pd


def rename_the_columns(df: pd.DataFrame) -> pd.DataFrame:
    """ Return the given dataframe df, which is read from the co2_emissions_vs_gdp.csv file,
    after changing the names of its columns to new names in the list new_names.

    Preconditions:
        - df is read from co2_emissions_vs_gdp.csv
    """
    new_names = ['country', 'code', 'year',
                 'total_population', 'continent', 'gdp_per_capita', 'co2_per_capita']
    df.columns = new_names
    return df


def country_dataframe(country: str, df: pd.DataFrame) -> pd.DataFrame:
    """ Return a new dataframe for the given country from the dataframe df, which is read
    from co2_emissions_vs_gdp.csv. The new dataframe has the following columns: country, year,
    co2_per_capita, gdp_per_capita, co2_per_gdp, and log_co2_per_gdp.
    It does not have any missing values.

    Preconditions:
    - df is read from co2_emissions_vs_gdp.csv
    - country is one of the countries in the df dataframe

    >>> finland_df = country_dataframe('Finland', rename_the_columns(pd.read_csv('co2_emissions_vs_gdp.csv')))
    >>> finland_df.shape == (157, 6)
    True
    """
    country_df = rename_the_columns(df)
    country_df = country_df[country_df['country'] == country]
    country_df = country_df[['country', 'year', 'co2_per_capita', 'gdp_per_capita']]
    country_df = country_df.dropna()
    country_df = country_df.reset_index(drop=True)
    count_row = country_df.shape[0]
    co2_per_gdp = [country_df.co2_per_capita[i] / country_df.gdp_per_capita[i]
                   for i in range(0, count_row)]
    country_df['co2_per_gdp'] = co2_per_gdp
    log_co2_per_gdp = [math.log(country_df.co2_per_gdp[i], 10) for i in range(0, count_row)]
    country_df['log_co2_per_gdp'] = log_co2_per_gdp
    return country_df


def look_up_implement_year(country: str) -> int:
    """ Return the year the carbon tax was implemented in the given country.

    Preconditions:
    - country is one of the countries in the Data_Overall csv file

    >>> look_up_implement_year('Poland')
    1990
    """
    overall_data = pd.read_csv('Data_Overall.csv')
    year_list = [overall_data['Year of implementation'][i]
                 for i in range(0, len(overall_data))
                 if overall_data['Jurisdiction covered'][i] == country]
    return int(year_list[0])


def before_implement(df: pd.DataFrame, country: str) -> pd.DataFrame:
    """ Return a data frame, which only contains the observations for the years
    before the implementation of the tax initiative for the given df and country.

    Preconditions:
    - df is read from co2_emissions_vs_gdp.csv
    - country is one of the countries in the Data_Overall csv file and the df
    dataframe.
    """
    implement_year = look_up_implement_year(country)
    df_before = country_dataframe(country, df)
    before_year = df_before['year'] <= implement_year
    df_before = df_before[before_year]
    return df_before


def after_implement(df: pd.DataFrame, country: str) -> pd.DataFrame:
    """ Return a data frame, which only contains the observations for the years
    after the implementation of the tax initiative for the given df and country.

    Preconditions:
    - df is read from co2_emissions_vs_gdp.csv
    - country is one of the countries in the Data_Overall csv file and the df
    dataframe.
    """
    implement_year = look_up_implement_year(country)
    df_after = country_dataframe(country, df)
    after_year = df_after['year'] > implement_year
    df_after = df_after[after_year]
    return df_after


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'pandas', 'math'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
