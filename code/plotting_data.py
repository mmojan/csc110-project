"""CSC110 Fall 2020 Project: Plotting the Data

Instructions
===============================

This Python module contains functions that create scatter plots with a line
of best fit on data extracted from the csv file for individual countries.
This module uses numpy and matplotlib.
This module uses numpy and matplotlib.

Copyright Information
===============================

This file is Copyright (c) 2020 Mojan Majid, Kimiya Raminrad, Dorsa Molaverdikhani, Ayesha Nasir.
"""
# Libraries:
from typing import Tuple, List
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# importing functions from cleaning_data
from cleaning_data import before_implement, after_implement, look_up_implement_year

DATA_DF = pd.read_csv('co2_emissions_vs_gdp.csv')


# Main Function:
def create_plot(country: str, y_value: str, regression_slope: float,
                regression_constant: float) -> None:
    """
    Plots the line of linear regression lines before and after implementation.

    Preconditions:
        - country != ''
        - y_value != ''
        - y value is a column in the country dataframe
        - country is one of the countries in the Data_Overall csv file and
        co2_emissions_vs_gdp.csv.
    """
    # creating variables.
    year_implemented = look_up_implement_year(country)
    bf_df = before_implement(DATA_DF, country)
    af_df = after_implement(DATA_DF, country)
    x1, y1, m1, b1 = plotting_values(bf_df, 'year', y_value)
    x2, y2, m2, b2 = plotting_values(af_df, 'year', y_value)
    x1, y1, x2, y2 = [np.array(i) for i in [x1, y1, x2, y2]]

    plt.clf()  # to clear the plot if function is called multiple times.
    # Labeling axes, adding visual markers.
    plt.xlabel('Year')
    plt.ylabel(y_value.replace('_', ' '))
    plt.axvline(year_implemented)
    plt.text(year_implemented + 1, m1 * year_implemented + b1, 'Tax Implemented')

    # creating the scatter plot
    plt.plot(x1, y1, 'o')
    plt.plot(x1, m1 * x1 + b1)
    plt.plot(x2, y2, 'o')
    plt.plot(x2, m2 * x2 + b2)

    # plotting the linear regression line after implementation, just to visualize difference
    plt.plot(x2, regression_slope * x2 + regression_constant)
    # saving plot as a jpeg, to be used in the report.
    plt.savefig(f'{country}.jpeg')


# Helper Function:
def plotting_values(country_df: pd.DataFrame, x_column: str, y_column: str) \
        -> Tuple[List, List, float, float]:
    """
    Returns a tuple of x-axis, y-axis values for the plot, and m = slope and = y-intercept values
    for the line of best fit.

    Preconditions:
    - x_column != ''
    - y_column != ''
    - x_column and y_column are columns in the country dataframe
    - country_df consists of data only for one country
    """
    # setting x and y values
    x_values = list(country_df[x_column])
    y_values = list(country_df[y_column])

    # finding slope and intercept
    x = np.array(x_values)
    y = np.array(y_values)
    m, b = np.polyfit(x, y, 1)

    return (x_values, y_values, m, b)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'numpy', 'matplotlib.pyplot', 'pandas',
                          'cleaning_data'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
