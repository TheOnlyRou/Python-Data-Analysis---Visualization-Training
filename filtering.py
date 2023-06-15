import pandas as pd
import matplotlib.pyplot as plt


# The goal of this lesson is to learn how to extract logical information from data via filters.
def filtering_example(df, **kwargs):
    if 'column' in kwargs and 'filter' in kwargs and 'action' in kwargs:
        column = kwargs.get("column")
        filter_var = kwargs.get("filter")
        action = kwargs.get("action")
        if action == "equal":
            # Insert a boolean condition where filter is equal to column
            print(df[df[column] == filter_var][kwargs.get("show_only")])
        elif action == 'greater':
            # Insert a boolean condition where column is greater than filter
            print(df[df[column] > filter_var][kwargs.get("show_only")])
        elif action == 'between':
            # Using a condition where the value is in between two values
            print(df[df[column].between(filter_var[0], filter_var[1])][kwargs.get("show_only")].value_counts())
        elif action == 'isin':
            # Using a condition where the values from the column exist in some other list or data structure you provide
            print(df[df[column].isin(filter_var)][kwargs.get("show_only")])
        elif action == 'combined':
            # Using a combo of Filters. Can also use & or | to concatenate conditions
            for key, value in filter_var.items():
                df = df[df[key] == value]
            print(df[kwargs.get("show_only")])
        elif action == 'negate':
            # Using a combo of Filters with a tilde (~) to negate the condition.
            for key, value in filter_var.items():
                df = df[~(df[key] == value)]
            print(df[kwargs.get("show_only")])
    elif 'column' in kwargs and 'filter' in kwargs:
        column = kwargs.get("column")
        filter_var = kwargs.get("filter")
        if filter_var == 'NaN':
            print(df[df[column].isna()])
        elif filter_var == 'notNaN':
            print(df[df[column].isna()])


def plot_filter(df, **kwargs):
    if 'column' in kwargs and 'filter' in kwargs:
        column = kwargs.get("column")
        filter_var = kwargs.get("filter")
        df = df[filter_var]
        print(df)
        df.plot(kind=kwargs.get('plot_type'))
        plt.show()


def exercise(df, **kwargs):
    if 'sort_by' in kwargs:
        sort_by = kwargs.get('sort_by')
        ascending = kwargs.get('ascending')
        df = df.sort_values(sort_by, ascending=ascending)
    if 'filter' in kwargs:
        filter_var = kwargs.get("filter")
        df = df[filter_var]
    if 'column' in kwargs:
        column = kwargs.get("column")
        df = df[column]
    if 'value_counts' in kwargs:
        df = df.value_counts()
    if 'top' in kwargs:
        top = kwargs.get('top')
        df = df.head(top)
    if 'plot_type' in kwargs:
        plot_type = kwargs.get('plot_type')
        df.plot(kind=plot_type)
        plt.show()
    print(df)
    pass
