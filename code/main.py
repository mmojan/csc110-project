"""CSC110 Fall 2020 Project: Main Project File

Instructions
===============================

This Python module contains the main function which calls on several functions from
other files to generate the values from linear regression model and graphs a plot of
a country for the given y-axis value, including a line of best fit.

Copyright Information
===============================

This file is Copyright (c) 2020 Mojan Majid, Kimiya Raminrad, Dorsa Molaverdikhani, Ayesha Nasir.
"""
import webbrowser
import pandas as pd
from plotting_data import create_plot
from linear_regression import linear_regression_before, linear_regression_after
from report_generation import create_report

COUNTRIES_DATAFRAME = pd.read_csv('co2_emissions_vs_gdp.csv')


def country_linear_regression(country_name: str, y_axis: str) -> None:
    """
    Creates a scatter plot with lines of best fit for the given country against
    the values given as y_axis, also outputs the linear regression models in the console.

    Preconditions:
        - country_name != '' and y_axis != ''
        - country is a country in COUNTRIES_DATAFRAME
        - y_axis is a valid column name for the country in country dataframe.
    """
    m_before, b_before = linear_regression_before(COUNTRIES_DATAFRAME, country_name,
                                                  y_axis).values()
    m_after, b_after = linear_regression_after(COUNTRIES_DATAFRAME, country_name,
                                               y_axis).values()
    create_plot(country_name, y_axis, m_before, b_before)
    create_report(country_name, y_axis, [m_before, b_before, m_after, b_after])

    webbrowser.open_new(f'{country_name}_report.pdf')
    print(f'If the PDF file doesn\'t automatically open up in a web browser, '
          f'please navigate to the project folder and open up the file '
          f'{country_name}_report.pdf for visualized result.')


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'pandas',
                          'plotting_data', 'linear_regression',
                          'webbrowser', 'report_generation'],
        'allowed-io': ['country_linear_regression'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
