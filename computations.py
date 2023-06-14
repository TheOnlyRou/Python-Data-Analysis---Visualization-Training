import pandas as pd


def compute_basic(df: pd.DataFrame):
    print(df.min())
    print(df.max())
    print(df.sum())
    # sum only numerical values
    print(df.sum(numeric_only=True))
    print(df.count())

    # mean, mode and median
    print(df.mean())
    print(df.mode())
    print(df.median())

    # mean, mode and median with numeric values only. Notice the difference
    print(df.mean(numeric_only=True))
    print(df.mode(numeric_only=True))
    print(df.median(numeric_only=True))

    # Describing Numeric fields within the dataframe. Displays descriptive stats like percentiles, std, count,
    # variance, etc
    print(df.describe())

    # Include object datatype or more in the describe command:
    # Object can also be written as "O"
    print(df.describe(include="object"))
    # Include Objects and int64
    print(df.describe(include=["object", "int64"]))

    # get sum of population of us in 2010 census
    # Dataset includes populations in whole of US, west, east regions and Puerto Rico. Here we remove those.
    df.tail(52).head(51).sum(numeric_only=True)


def exercise(df: pd.DataFrame):
    print(f"Lowest User Rating: \n{df['User Rating'].min()}")
    print(f"Highest Price: \n{df['Price'].max()}")
    print(f"Average User Rating: \n{df['User Rating'].mean()}")
    print(f"Average User Rating of first 5: \n{df['User Rating'].head().mean()}")
    print(f"Most occurring User Review: \n{df['Reviews'].mode()}")
    print(f"Unique Number of Authors: \n{df['Author'].describe().loc[['unique']]}")
    print(f"Author with most books: \n{df['Author'].describe().loc[['top']]}")

