import pandas as pd


def rename_col(df, columns1: list, columns2: list):
    mapper = {}
    for col in columns1:
        mapper[col] = columns2[columns1.index(col)]
    df.rename(columns=mapper, inplace=True)
    print(df)


def rename_row(df, rows1: list, rows2: list):
    mapper = {}
    for row in rows1:
        mapper[row] = rows2[rows1.index(row)]
    df.rename(index=mapper, inplace=True)
    print(df)


def replace_value(df, column, value, new_value):
    # Value and new value can be object or list to replace several values
    df[column].replace(value, new_value, inplace=True)
    print(df)


def exercise(df, **kwargs):
    if 'index' in kwargs:
        index = kwargs.get("index")
        if 'inplace' in kwargs:
            df.set_index(index, inplace=kwargs.get('inplace'))
        else:
            df.set_index(index)
    if 'find' in kwargs:
        find = kwargs.get("find")
        if 'column' in kwargs & 'replace_value' in kwargs:
            column = kwargs.get("column")
            replace_val = kwargs.get("replace_value")
            df[column].loc[find, column] = replace_val
    if 'rename' in kwargs:
        rename = kwargs.get("rename")
        new_name = kwargs.get("new_name")
        if 'inplace' in kwargs:
            df.rename(columns={rename, new_name}, inplace=kwargs.get('inplace'))
        else:
            df.rename(columns={rename, new_name})
    if 'loc' in kwargs:
        loc = kwargs.get("loc")
        col = kwargs.get("col")
        change_index = kwargs.get("change_index")
        if 'inplace' in kwargs:
            df.loc[col == loc, "show_id"] = change_index
    if 'new_col' in kwargs:
        filt = kwargs.get("predicate")
        new_col = kwargs.get('new_col')
        default_val = kwargs.get("default_val")
        value = kwargs.get("value")
        df[new_col] = default_val
        condition = df[kwargs.get("column")].isin(filt)
        df[condition] = value


