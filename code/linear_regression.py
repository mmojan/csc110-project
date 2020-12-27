"""CSC110 Fall 2020 Project: Linear Regression

Instructions
===============================

This Python module contains several functions that fit linear regression lines
to our data for years before and after the implementation of a tax initiative.

Copyright Information
===============================

This file is Copyright (c) 2020 Kimiya Raminrad, Mojan Majid, Dorsa Molaverdikhani, Ayesha Nasir.
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import cleaning_data


def linear_regression_before(df: pd.DataFrame, country: str, y: str) -> dict:
    """ Return a dictionary which has two keys, the slope and intercept, and their values for
    the fitted regression line for the given df, country, and y that we choose.
    For example, we can choose y to be log_co2_per_gdp or co2_per_gdp.
    The predictor x is the years before the implementation of a tax.

     Preconditions:
    - df is read from co2_emissions_vs_gdp.csv
    - country is one of the countries in the df dataframe
    - y is a name between the name of columns in our data

    >>> linear_regression_before(pd.read_csv('co2_emissions_vs_gdp.csv'), "Finland", 'log_co2_per_gdp')
    {'Slope': 0.01215790840011023, 'Intercept': -27.35641825702518}
    >>> linear_regression_before(pd.read_csv('co2_emissions_vs_gdp.csv'), "Finland", 'co2_per_gdp')
    {'Slope': 4.271543163206262e-06, 'Intercept': -0.008024786836634653}
    """
    df1 = cleaning_data.before_implement(df, country)
    y = df1[y]
    x = df1['year']
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)
    coefficient = ("Coefficient:", model.coef_[0])
    intercept = ("Intercept:", model.intercept_)

    return {'Slope': coefficient[1], 'Intercept': intercept[1]}


def linear_regression_after(df: pd.DataFrame, country: str, y: str) -> dict:
    """ Return a dictionary which has two keys, the slope and intercept, and their values for
    the fitted regression line for the given df, country, and y that we choose.
    For example, we can choose y to be log_co2_per_gdp or co2_per_gdp.
    The predictor x is the years after the implementation of a tax.

     Preconditions:
    - df is read from co2_emissions_vs_gdp.csv
    - country is one of the countries in the df dataframe
    - y is a name between the name of columns in our data

    >>> linear_regression_after(pd.read_csv('co2_emissions_vs_gdp.csv'), "Finland", 'log_co2_per_gdp')
    {'Slope': -0.01275374010180578, 'Intercept': 22.079352956658287}
    >>> linear_regression_after(pd.read_csv('co2_emissions_vs_gdp.csv'), "Finland", 'co2_per_gdp')
    {'Slope': -9.837319210474738e-06, 'Intercept': 0.020054768575273888}
    """
    df1 = cleaning_data.after_implement(df, country)
    y = df1[y]
    x = df1['year']
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:, np.newaxis], y)
    coefficient = ("Coefficient:", model.coef_[0])
    intercept = ("Intercept:", model.intercept_)

    return {'Slope': coefficient[1], 'Intercept': intercept[1]}


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'pandas', 'math',
                          'numpy', 'sklearn.linear_model', 'cleaning_data'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
