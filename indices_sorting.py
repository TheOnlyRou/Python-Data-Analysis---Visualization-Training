import pandas as pd
import matplotlib.pyplot as plt


# Goal of this section is to learn why one would want to index a dataframe with a non numeric index and how that would
# be done, as well as learning to sort dataframes and series
def indices_example(df, **kwargs):
    print(df.info())
    if 'uppercase_filter' in kwargs:
        # Converts the values to lowercase when comparing values for sorting
        df.sort_values(kwargs.get("sort_by"), ascending=False,
                       key=lambda col: col.str.lower())
        print(df)
    if 'sort_by' in kwargs:
        if kwargs.get('sort_by') == 'index':
            df.sort_index(ascending=False)
            print(df)
    if 'column' in kwargs:
        # Use set_index to set a new index for the dataframe. Use inplace to change the index of the passed dataframe,
        # or don't use inplace to return a new df with the returned new index
        df.set_index(kwargs.get("column"), inplace=True)
        if 'var_plot' in kwargs:
            df[kwargs.get('var_plot')].plot(kind=kwargs.get('plot_type'))
            plt.show()
            if 'sort_by' in kwargs:
                # Sort values by a certain column or columns, can be ascending or descending. Executes an alphabetical
                # or numerical sort
                df.sort_values(kwargs.get("sort_by"), ascending=False)[kwargs.get('var_plot')] \
                    .plot(kind=kwargs.get('plot_type'))
                plt.show()


# Using loc & iloc to locate data by its label (Locate Row)
def loc_iloc_example(df, **kwargs):
    # Make sure to strip your index column of any trailing or leading whitespaces if it's an alphanumerical index
    df[kwargs.get("column")] = df[kwargs.get("column")].str.strip()
    # Make sure to perform the whitespace stripping step before setting your index, as it will not work afterwards as
    # the column becomes the index
    df.set_index(kwargs.get("column"), inplace=True)
    print(df)
    # Using loc to get a range, conditional or value
    print(df.loc[kwargs.get('loc')])
    # Using loc to get range, conditional, or value and return only a set of columns ("filters")
    print(df.loc[kwargs.get('loc'), kwargs.get("filters")])

    # You can also use iloc to search by index in the series/dataframe


def exercise(df, **kwargs):
    if 'index' in kwargs:
        # Remember to remove any leading or trailing whitespaces.
        df[kwargs.get("index")] = df[kwargs.get("index")].str.strip()
        df.set_index(kwargs.get("index"), inplace=True)
    if 'sort_by' in kwargs:
        if kwargs.get("sort_by") == 'index':
            print(df.sort_index(inplace=True))
        else:
            print(df.sort_values(kwargs.get("sort_by"), ascending=kwargs.get("ascending"))[kwargs.get("find")])
            df = df.sort_values(kwargs.get("sort_by"), ascending=kwargs.get("ascending"))[kwargs.get("find")]
            if 'first' in kwargs:
                if kwargs.get("action") == 'avg':
                    mean = df.head(kwargs.get("first")).mean()
                    print(f"Avg speed of top 10 speeds: \n{str(mean)}")
                elif kwargs.get("action") == 'mode':
                    mode = df.head(kwargs.get("first")).value_counts().head(1)
                    print(mode)
    if 'retrieve' in kwargs:
        print(df.loc[kwargs.get("retrieve")])
        df = df.loc[kwargs.get("retrieve")]
    if 'iretrieve' in kwargs:
        print(df.iloc[kwargs.get("iretrieve")])
        df = df.iloc[kwargs.get("iretrieve")]
    if 'retrieve_from' in kwargs:
        print(df.loc[kwargs.get("retrieve_from"):kwargs.get("retrieve_to")])
        df = df.loc[kwargs.get("retrieve_from"):kwargs.get("retrieve_to")]
    if 'plot' in kwargs:
        df = df.sort_values()
        df.plot(kind=kwargs.get('plot'))
        plt.show()
