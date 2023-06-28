import pandas as pd


def concat_series_vertically(s1, s2):
    # Concatenating series on top of each other
    # Beware that order determines which series appears first
    # Index is preserved from original series. Can be ignored with parameter ignore_index = True
    # Dtype of resulting series dependent on compatibility. Default is object. Consider casting your result
    pd.concat([s1, s2])

def concat_series_horizontally(s1,s2):
    # Results in a dataframe
    # To do so, just add parameter axis = 1

    pd.concat([s1,s2], axis = 1, ignore_index=True)

    # Note that if the index is compatible, it concatenates using the index, meaning that if values are shuffled in a series but not the s1,
    # the resultant dataframe will have the 2nd series sorted by the index that both are compatible with

    # ex: a: apple, b: banana, c: cherry - b: badger, a:animal , c: cougar
    # Result of concatenating these 2 series will result in

    # a: apple      animal
    # b: banana     badger
    # c: cherry     cougar


def concat_series_non_compat_index(s1,s2):
    # If an index in s1 is non compatible in s2 "No corresponding value" the result in the 2nd column in that index
    # will be a NaN
    # Only shows values with corresponding index in both series
    pd.concat([s1,s2], axis=1, join="inner")
    # Shows all indices and values. Non corresponding values will result in NaN
    pd.concat([s1, s2], axis=1, join="outer")


def merge_example(df1,df2):
    # Merge 2 dataframes based on their data content. Looks for similar values to merge both dfs.
    # Can specify to merge on which column. Use on parameter to find common value to merge on
    # Can use which type of join as well. Default join type is inner
    df1.merge(df2)

