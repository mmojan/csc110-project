"""CSC110 Fall 2020 Project: Report Generation

Instructions
===============================

This Python module contains a function which takes the plot image generated from
plotting_data.py and values generated from linear_regression to output a pdf
file with comparison of values.

Copyright Information
===============================

This file is Copyright (c) 2020 Mojan Majid, Kimiya Raminrad, Dorsa Molaverdikhani, Ayesha Nasir.
"""
from typing import List
from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate, Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet


def create_report(country: str, y_axis: str, values: List) -> None:
    """
    Creates a pdf file with the generated plot image and text.

    Preconditions:
        - country != ''
        - y_axis != ''
        - values != []
        - country is a country in co2_emissions_vs_gdp.csv
        - y_axis is a column in the country's dataframe
        - create_report is called from the main function
        - create_report is called with correct linear regression model values.
    """
    # unpacking variables:
    m_b, b_b, m_a, b_a = values
    # text to be used:
    doc_title = f'The Effectiveness of {country}\'s Carbon Tax Policy on Reducing ' \
                f'CO2 Emissions.'
    doc_intro = f'In this instance of our program, we are testing the effectiveness of ' \
                f'{country}\'s policy of Carbon Tax. Our program generates a scatter plot ' \
                f'of the {y_axis} of the country against the years since data was being ' \
                f'collected.'
    para_1 = f'We generate the slope and coefficient of the linear regression lines' \
             f' using this data Before the carbon tax was implemented, the linear regression ' \
             f'line for the country of {country} has the slope {m_b} and ' \
             f'the y-intercept as {b_b}. After the carbon  tax implementation, ' \
             f'the linear regression line was found to have the slope {m_a} and ' \
             f'the y-intercept to be {b_a}. The plotted values of the country\'s ' \
             f'{y_axis} against years is shown in a plot.'
    tax_successful = f'From our plotted values and the slopes of linear regression model ' \
                     f'generated before and after the tax implementation, we can see that there ' \
                     f'is sizeable difference between the slopes of linear regression model ' \
                     f'before and after the implementation: the difference is greater than half ' \
                     f'the size of the slope before implementation. ' \
                     f'Thus, we may be able to conclude that the implementation of Carbon Tax by ' \
                     f'{country} has been successful in reducing co2 emissions '
    tax_unsuccessful = f'From our plotted values and the slopes of linear regression model ' \
                       f'generated before and after the tax implementation by {country}, the ' \
                       f'difference between the slope of the linear regression before the tax ' \
                       f'implementation and the slope of the model after the tax implementation ' \
                       f'isn\'t significant enough for us to properly conclude something.'

    # creating a basic document
    doc = SimpleDocTemplate(f'{country}_report.pdf', pagesize=letter, rightMargin=72,
                            leftMargin=72, topMargin=72, bottomMargin=18,
                            title=f'Effectiveness of {country}\'s Tax Policy on '
                                  f'Reducing Carbon Emission',
                            author='Ayesha Nasir, Kimia Raminrad, Mojan Majid, '
                                   'Dorsa Molaverdi')
    styles = getSampleStyleSheet()  # for the styles used in the document.
    story = []
    story.append(Paragraph(doc_title, styles['Title']))
    story.append(Spacer(1, 12))
    story.append(Paragraph(doc_intro, styles['BodyText']))
    story.append(Paragraph(para_1, styles['BodyText']))
    story.append(Spacer(1, 12))
    # Adding the generated plot to the pdf
    story.append(Image(f'{country}.jpeg', 400, 300))

    # adding the proper result.
    if m_a < m_b / 2:
        story.append(Paragraph(tax_successful, styles['BodyText']))
    else:
        story.append(Paragraph(tax_unsuccessful, styles['BodyText']))

    # creating the final PDF file.
    doc.build(story)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'reportlab',
                          'reportlab.platypus', 'reportlab.lib.styles',
                          'reportlab.lib.pagesizes', 'typing'],
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
