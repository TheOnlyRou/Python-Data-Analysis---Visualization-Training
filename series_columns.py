import pandas as pd
import matplotlib.pyplot as plt


# How to select a single column from a dataframe?
# Use df['column_name'] or df.column_name
# However, using the df['column_name'] is more reliable and provides more functionalities
# Particularly the . notation fails when there's a whitespace or a special character ($#@!$(*_ &) in the column name
# Additionally, the . notation fails when there's column names that reference package methods/properties like
# head, tail, etc.
# Also, the ['column_name'] notation allows you to select multiple columns or use variables to fetch the Series
# Using this notation returns a Series object, which is basically a vector with the same length as the original
# dataframe, but with the data of the selected column only


# To be used on the titanic dataset
def selected_series_method_showcase(df, column_name):
    # Fetch the names Series because column_name is a String
    s = df[column_name]

    # Important Series methods
    # head(), tail(), describe(), unique(), nunique(), nlargest(), nsmallest(), value_counts(), plot()

    # Returns all unique values in this series
    print(s.unique)

    # Returns a count of all unique values in this series
    print(s.nunique)

    # To display NaN values in the unique count
    # By default, dropna is True in nunique() and False in unique()
    print(s.nunique(dropna=False))

    # Display how many times all values occurred
    print(s.value_counts())

    # Display only a subset of the value count
    print(s.value_counts().head(10))

    # Get the largest and smallest n values in the series. Default is 5
    print(s.nsmallest())
    print(s.nlargest(10))

    # To keep duplicates in this method, add a keep flag with values 'first', 'last' or 'all'
    print(s.nlargest(10, keep='all'))

    # To apply nlargest or nsmallest on the Dataframe. Add the column names to the function to parameter columns
    # as a list
    print(df.nlargest(10, columns=[column_name]))


def selected_dataframe_method_showcase(df, columns):
    # fetch a sub dataframe since the columns var is a List
    sub_df = df[columns]
    print(sub_df.describe())

    # Display how many times the combination of the provided column values occurred in the dataset
    # Returns a multi-column indexed Series.
    print(sub_df.value_counts())


def basic_visualisation(df, column_name, columns):
    # Basic plot kind is line plot
    # Print the plot of a series. Not so informative
    if df[column_name].dtypes == 'int64':
        print(df[column_name].plot())

    # More informative
    df_plot = df[column_name].value_counts().plot()
    plt.show()

    # Make it a bar graph for more readability
    print(df[column_name].value_counts().plot(kind="bar"))
    plt.show()


def exercise(df, **kwargs):
    if 'column_name' in kwargs:
        s = df[kwargs.get('column_name')]
        if kwargs.get('ex') == 1:
            print(s.head(8))
        elif kwargs.get('ex') == 2:
            print(s.unique())
            print(s.nunique())
        elif kwargs.get('ex') == 3:
            print(s.value_counts().head(3))
        elif kwargs.get('ex') == 4:
            print(s.count())
            if s.count() > 10:
                s.value_counts().head(10).plot(kind=kwargs.get('plot_type'))
                plt.show()
            else:
                s.value_counts().plot(kind=kwargs.get('plot_type'))
                plt.show()
        elif kwargs.get('ex') == 4.4:
            if s.dtypes == 'float64':
                s.plot(kind=kwargs.get('plot_type'))
            plt.show()
        if s.dtypes == 'int64':
            print(f"Mean of the series:\n{s.mean()}")
            print(f"Largest in the series: \n{s.nlargest(10)}")
    if 'columns' in kwargs:
        if kwargs.get('ex') == 3:
            print(df[kwargs.get('columns')])
            print(df[kwargs.get('columns')].value_counts())
        elif kwargs.get('ex') == 4:
            df[kwargs.get('columns')].value_counts().head(10).plot(kind='barh')
            plt.show()
        for column in kwargs.get('columns'):
            s = df[column]
            if kwargs.get('ex') == 1:
                print(s)
            elif kwargs.get('ex') == 2:
                print(s.unique())
                print(s.nunique())
                if s.dtypes == 'int64':
                    print(s.mean())
                    print(s.nlargest(10))






