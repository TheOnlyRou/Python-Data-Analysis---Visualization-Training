import pandas as pd

# It all revolves around the pd function pd.to_datetime(The DateTime String)
# References:
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior,
# https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html


def parse_time(df, col):
    print(df.info())
    df[col]=pd.to_datetime(df[col])
    print(df)


def get_datetime_properties(df, col):
    print("Distribution of Sightings against Months\n", df[col].dt.month.value_counts().astype("int64"))
    print("Distribution of Sightings against Days\n",df[col].dt.day.value_counts().astype("int64"))
    print("Distribution of Sightings against Time of the day\n", df[col].dt.hour.value_counts().astype("int64"))
