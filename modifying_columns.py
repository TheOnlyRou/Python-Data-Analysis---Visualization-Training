import pandas as pd
import matplotlib.pyplot as plt


def drop_columns(df, columns):
    # axis = 1 or axis ='columns' means columns from the dataframe
    df.drop(labels=columns, axis=1, inplace=True)
    print(df)
    pass


def drop_rows(df, rows):
    # axis = 0 means rows from the dataframe
    df.drop(labels=rows, axis=0, inplace=True)
    print(df)


def add_rows(df, rows):
    pass


def add_columns(df, col_names, cols):
    # cols can be a String, or a Series
    for col in col_names:
        df[col_names] = cols[col_names.index(col)]
    print(df)


def clone_col(df, col, new_col):
    df[new_col] = col
    print(df)


def clone_col_at_index(df, col, new_col, index):
    df.insert(index, new_col, col)
    print(df)


def exercise(df, **kwargs):
    if 'index' in kwargs:
        index = kwargs.get("index");
        df = df.set_index(index)
    if 'drop_col' in kwargs:
        drop_col = kwargs.get("drop_col")
        df.drop(labels=drop_col, axis=1, inplace=True)
    if 'drop_row' in kwargs:
        drop_row = kwargs.get("drop_row")
        df.drop(labels=drop_row, axis=0, inplace=True)
    if 'add_col' in kwargs:
        add_col = kwargs.get("add_col")
        if 'add_value' in kwargs:
            add_value = kwargs.get("add_value")
            df[add_col] = add_value
        if 'filter' in kwargs:
            filter_col = kwargs.get("filter")
            df[add_col] = filter_col
    if "sort_by" in kwargs:
        sort_by = kwargs.get("sort_by")
        ascending = kwargs.get("ascending")
        df.sort_values(sort_by, ascending=ascending)
    if "head" in kwargs:
        head = kwargs.get("head")
        df = df.head(head)
    print(df)



