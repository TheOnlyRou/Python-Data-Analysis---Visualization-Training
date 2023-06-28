import pandas as pd


def years_to_days(yrs):
    return yrs * 365


def age_group(age):
    if age < 2:
        return 'infant'
    elif age < 12:
        return "child"
    elif age < 20:
        return "teen"
    elif age < 45:
        return "adult"
    else:
        return "senior"


def change_currency(num, multiplier):
    return f"${num * multiplier}"


def apply_func(df, col, func):
    df[col].apply(func)

    df["age_group"] = df[col].apply(func)


def apply_func_lambda(df, col):
    df[col].apply(lambda x: f"${x * 24}")


def apply_func_args(df, col, args):
    # The apply passes the df or df[col] element to your function as first arg
    # Can also use kwargs and they will just be passed to your function as is
    df[col].apply(change_currency, args=(2,))


def get_fam_size(s):
    # Only works on Titanic dataset
    # Can be called by calling apply with axis = 1
    fam_size = s.sibsp + s.parch
    if fam_size == 0:
        return "Solo"
    elif fam_size < 5:
        return 'Avg Fam'
    else:
        return "Large"


def map_example(s):
    # Map is a Series only function that takes every single value from a series/dict/func and maps it onto values from another series
    # Example: pclass from Titanic dataset
    s.map({1: "1st", 2: "2nd", 3: "3rd"})

    # Can also use Lambda functions


def applymap_exampe(df):
    # Dataframe only function that takes a dataframe and runs a function on the whole dataframe.
    df.applymap(str.upper)

    df.applymap(lambda el: el**3)
