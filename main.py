import pandas as pd
import matplotlib.pyplot as plt

import computations as comp
import dataframes as dataf
import series_columns as sc
import indices_sorting as ind
import filtering as filt
import modifying_columns as mdf
import updating_values as upd
import datetime_manipulation as dtm
import matplotlib_practice as mat
import grouping_aggregating as grp
import functions_apply as f
import combining_dataframes as comb
import seaborn_training as sea


def get_dataframes():
    dataf.get_bestsellers_example()
    dataf.get_everest_example()
    dataf.get_movietitles_example()
    dataf.get_houses_example()
    dataf.get_titanic_example()
    dataf.get_netflix_example()


def section2():
    comp.compute_basic(dataf.get_bestsellers_example())
    comp.compute_basic(dataf.get_everest_example())
    comp.compute_basic(dataf.get_movietitles_example())
    comp.compute_basic(dataf.get_houses_example())
    comp.compute_basic(dataf.get_titanic_example())
    comp.compute_basic(dataf.get_netflix_example())
    comp.exercise(dataf.get_bestsellers_example())


def section3():
    sc.selected_series_method_showcase(dataf.get_houses_example(), 'price')
    sc.selected_dataframe_method_showcase(dataf.get_titanic_example(), ['name', 'sex'])
    sc.basic_visualisation(dataf.get_houses_example(), 'bedrooms', ['bedrooms', 'bathrooms'])
    sc.basic_visualisation(dataf.get_netflix_example(), 'rating', [])
    print(dataf.get_bestsellers_example().describe())
    # Part 1 Exercise
    sc.exercise(dataf.get_bestsellers_example(), column_name='Author', ex=1)
    sc.exercise(dataf.get_bestsellers_example(), columns=['Name', 'User Rating'], ex=1)
    # Part 2 Exercise
    sc.exercise(dataf.get_bestsellers_example(), column_name='Genre', ex=2)
    sc.exercise(dataf.get_bestsellers_example(), column_name='Author', ex=2)
    sc.exercise(dataf.get_bestsellers_example(), column_name='Price', ex=2)
    # Part 3
    sc.exercise(dataf.get_bestsellers_example(), column_name='Name', columns=['Author', 'User Rating'], ex=3)
    # Part 4
    sc.exercise(dataf.get_bestsellers_example(), column_name='Genre', ex=4, plot_type="pie")
    sc.exercise(dataf.get_bestsellers_example(), column_name='Author', plot_type='barh', ex=4)
    sc.exercise(dataf.get_bestsellers_example(), column_name='User Rating', ex=4.4, plot_type="hist")


def section4():
    ind.indices_example(dataf.get_bitcoin_example(), column='Date', var_plot='High', plot_type='line')
    ind.indices_example(dataf.get_happiness_example(), column='Country name', var_plot='Healthy life expectancy',
                        plot_type='line', sort_by='Healthy life expectancy')
    ind.indices_example(dataf.get_titanic_example(), sort_by='name', uppercase_filter=True)
    ind.indices_example(dataf.get_countries_example(), sort_by='index')
    ind.loc_iloc_example(dataf.get_countries_example(), loc=["Yemen", "United States", "Egypt"], column="Country",
                         filters=["Region", "Population"])

    # Exercises
    ind.exercise(dataf.get_pokemon_example(), index="Name", sort_by="Attack", find="Attack", ascending=False)
    ind.exercise(dataf.get_pokemon_example(), index="Name", sort_by="Num", find="Num", ascending=True)
    ind.exercise(dataf.get_pokemon_example(), index="Name", sort_by=["Num", "Attack"], find=["Num", "Attack"],
                 ascending=False)
    ind.exercise(dataf.get_pokemon_example(), index="Name", sort_by="index", ascending=True)
    ind.exercise(dataf.get_pokemon_example(), sort_by="Speed", first=10, action="avg", find="Speed", ascending=False)
    ind.exercise(dataf.get_pokemon_example(), sort_by="Attack", first=20, action="mode", find="Type 1", ascending=False)
    ind.exercise(dataf.get_pokemon_example(), index="Name", retrieve="Diglett")
    ind.exercise(dataf.get_pokemon_example(), index="Name", retrieve=["Eevee", "Vulpix"])
    ind.exercise(dataf.get_pokemon_example(), index="Name", sort_by="index", retrieve_from="Charizard",
                 retrieve_to="Charmeleon", ascending=True)
    ind.exercise(dataf.get_pokemon_example(), index="Name", iretrieve=[30, 40, 50])
    ind.exercise(dataf.get_pokemon_example(), index="Name",
                 retrieve=["Magikarp", "Goldeen", "Horsea", "Seaking", "Seadra", "Gyarados"], plot="bar",
                 sort_by="Attack", find="Attack", ascending=True)


def section5():
    # # Get all females on the titanic dataset
    # filt.filtering_example(dataf.get_titanic_example(), action='equal', column='sex', filter='female', show_only="name")
    # # Get all houses with price of greater than 5,000,000
    # filt.filtering_example(dataf.get_houses_example(), action='greater', column='price', filter=5000000,
    #                        show_only="price")
    # # Get all houses with between 3 and 5 bedrooms
    # filt.filtering_example(dataf.get_houses_example(), action='between', column='bedrooms', filter=[3, 5],
    #                        show_only="bedrooms")
    # # Get all females on the titanic dataset that died
    # filt.filtering_example(dataf.get_titanic_example(), column="sex", action="combined", filter={"sex": "female", "survived": 0}, show_only=["name", "sex", "pclass"])
    # # Get the opposite of the above example. Get all men that lived by applying opposite.
    # filt.filtering_example(dataf.get_titanic_example(), column="sex", action="negate",
    #                        filter={"sex": "female", "survived": 0}, show_only=["name", "sex", "pclass"])
    # # Get all shows/movies where director is NaN (Unknown)
    # filt.filtering_example(dataf.get_netflix_example(), column="director", filter="NaN")
    # # Get all shows/movies where director is known
    # filt.filtering_example(dataf.get_netflix_example(), column="director", filter="notNaN")
    # titanic = dataf.get_titanic_example()
    # women = titanic['sex'] == 'female'
    # survived = titanic['survived'] == 1
    # filt.plot_filter(titanic, column="sex", filter=women & survived, plot_type = "bar")

    # Exercise
    # Get all books written by Pete Souza
    bestsellers = dataf.get_bestsellers_example()
    filt.exercise(bestsellers, column="Name", filter=bestsellers['Author'] == 'Pete Souza')
    # Get all books under 10$
    filt.exercise(bestsellers, column="Name", filter=bestsellers['Price'] < 10)
    # Get all books between 50$ & 60$
    filt.exercise(bestsellers, column="Name", filter=bestsellers['Price'].between(50, 60))
    # Get all books written by Kristin Hannah or Andy Weir or Delia Owens
    authors = ['Kristin Hannah', 'Andy Weir', 'Delia Owens']
    filt.exercise(bestsellers, column='Name', filter=bestsellers['Author'].isin(authors))
    # Get all Non fiction books that are rated 4.9
    non_fiction = bestsellers['Genre'] == 'Non Fiction'
    user_rated = bestsellers['User Rating'] == 4.9
    filt.exercise(bestsellers, column=['Name', 'User Rating', "Genre"], filter=non_fiction & user_rated)
    # Get fiction book with lowest rating
    filt.exercise(bestsellers, column=['Name', 'User Rating'], sort_by="User Rating", top=1, ascending=True,
                  filter=~non_fiction)
    # Get 2012's top 5 fiction book with most reviews
    year2012 = bestsellers['Year'] == 2012
    fiction = bestsellers['Genre'] == 'Fiction'
    filt.exercise(bestsellers, sort_by="Reviews", top=5, filter=year2012 & fiction, ascending=False)
    # Bar plot of 5 authors who have most books with rating under 4.5
    filt.exercise(bestsellers, sort_by=['Author', 'User Rating'], top=5, filter=bestsellers['User Rating'] < 4.5,
                  plot_type="barh", value_counts=True, ascending=False, column=['Author', 'User Rating'])


def section6():
    # Set id as index
    tweets = dataf.get_tweets_example()
    mdf.exercise(tweets, index="id")
    # Drop url column
    mdf.exercise(tweets, drop_col="url")
    # Drop 361388562
    mdf.exercise(tweets, index='id', drop_row=361388562)
    # New column 'user', value='Joe Biden'
    mdf.exercise(tweets, add_col='user', add_value='Joe Biden')
    # New column get ratio
    mdf.exercise(tweets, add_col='ratio', filter=tweets['replies'] / tweets['retweets'], head=10, sort_by='ratio',
                 ascending=False)
    # Get interactions with tweet
    mdf.exercise(tweets, add_col='interactions', filter=tweets['replies'] + tweets['retweets'] + tweets['likes'] +
                                                        tweets['quotes'], head=10, sort_by='interactions',
                 ascending=False)

def section7():
    titanic = dataf.get_titanic_example()
    upd.replace_value(titanic, "sex", "Female", "F")
    upd.replace_value(titanic, "sex", ["Female", "Male"], ["F", "M"])
    # To replace unknown values set to some random value by None that doesn't show in stats, use the list notation.
    upd.replace_value(titanic, "age",  ["?"], [None])

    happiness = dataf.get_happiness_example()

    happiness.set_index("Country name", inplace = True)
    print(happiness)
    happiness.sort_index(inplace=True)
    print(happiness.loc["Brazil", ["Ladder score", "Healthy life expectancy"]])
    # Replace can be done using Loc. and can also be used to create new columns and set their values. In this case,
    # we add new column "isCold"
    happiness.loc[["Finland", "Denmark", "Iceland", "Sweden", "Norway"], ['Regional indicator', 'isCold']] = ["Nordic Country", "Y"]
    print(happiness.loc[["Finland", "Denmark", "Iceland", "Sweden", "Norway"]])

    houses = dataf.get_houses_example()
    # Get houses with more than 10 bedrooms
    print(houses[houses["bedrooms"] >= 10].loc[:, ["id", "bedrooms"]])

    # Use a boolean mask with loc
    houses.loc[houses["bedrooms"] >= 10, ["bedrooms"]] = "10+"

    netflix = dataf.get_netflix_example()
    print(netflix.info())
    upd.exercise(netflix, index="show_id", inplace=True)
    upd.exercise(netflix, find="s2202", column="director", replace_value="Greg Whiteley")
    upd.exercise(netflix, find=["s2881", "s3601"], column="duration", replace_value="GONE TOO SOON")
    upd.exercise(netflix, rename="release year", new_name="release yr", inplace=True)
    upd.exercise(netflix, loc="Evil", column="title", change_index="s6666", inplace=True)
    upd.exercise(netflix, new_col="is_fav", default_val="False", column="title", predicate=["Young Royals", "Dark", "Big Mouth",
                                                                            "BoJack Horseman", "The Queen's Gambit",
                                                                            "American Vandal", "Russian Doll",
                                                                            "Godless"], value=True)


def section8():
    # Datatypes in Pandas: Object, int64, float64, bool, datetime64, timedelta[ns], category
    titanic = dataf.get_titanic_example()
    # Remove unknown values and place None instead
    titanic["age"].replace(["?"], [None], inplace=True)
    print(titanic["age"].value_counts())
    # Change datatype to float
    titanic["age"] = titanic["age"].astype("float")
    # Now you can perform numeric computations and comparisons like mean()
    print("Mean Age: ", titanic["age"].mean())
    titanic["sex"] = titanic["sex"].astype("category")
    print(titanic["sex"])

    titanic = dataf.get_titanic_example()
    # Takes a series and converts it to numeric.
    # Default is to raise exception if it finds an error. Can use "coerce" to convert errors to NaN.
    # "ignore" will just return the input
    pd.to_numeric(titanic["age"], errors="coerce")

    # A helper function that determines if a value is na or not.
    stats = dataf.get_gamestats_example()
    print(stats.isna())
    print(stats["league"].isna())

    # dropna() Helper function to drop NA values

    # Using it with a series is pretty simple
    print(stats["assists"].dropna())

    # Using it on the whole dataframe
    print(stats.dropna())
    # Can also use more args to make
    # how: "any" or "all" that either drops row if ANY na value is found or if ALL values are na
    print(stats.dropna(how="all"))
    # subset: drop only if subset is na
    print(stats.dropna(subset=["league"]))

    # Another way to deal with NaN values is to fill NA values with some default value
    # Using it on an entire dataframe
    print(stats.fillna(0))
    # Using it on a certain series
    print(stats["rebounds"].fillna(0))
    print(stats["league"].fillna("amateur"))

    # can use it on an entire dataframe but specify which columns and values to replace
    print(stats.fillna({"points": 0, "assists": 0}))

    # Another way is to fill it with a vlaue from another column
    sales = dataf.get_sales_example()
    print(sales["shipping_zip"].fillna(sales["billing_zip"]))

    netflix = dataf.get_netflix_example()
    print("Dataframe Info:\n", netflix.info())
    # Get rows with no country
    print(netflix.loc[netflix["country"].isna()])

    print(netflix[["country", "director", "cast"]])
    # Get rows with no director, cast & country
    no_country = netflix["country"].isna()
    country_notna = ~netflix["country"].isna()
    no_cast = netflix["cast"].isna()
    no_director = netflix["director"].isna()
    print(netflix[no_country & no_director & no_cast])
    print(netflix[country_notna & no_director & no_cast])

    # Drop rows with any na values
    print(netflix.dropna(how="any"))
    # Drop columns with any NA values
    print(netflix.dropna(how="any", axis=1))

    print(netflix.dropna(subset=["director", "cast"]))

    netflix["rating"].loc["na"] = "TV-MA"
    print(netflix["rating"])
    print("Country Value Counts:\n", netflix["country"].value_counts().sort_values(ascending=False))
    print("Country Mode:\n", netflix["country"].mode())
    netflix.loc[no_country] = None
    mode = netflix["country"].mode()[0]
    netflix["country"].fillna(mode, inplace=True)
    # can also be done like this:
    netflix.fillna({"country": mode}, inplace=True)
    print(netflix["country"])
    pass


def section9():
    # ufos = dataf.get_ufos_example()
    # dtm.parse_time(ufos, "date_time")
    # dtm.get_datetime_properties(ufos, "date_time")

    # Exercise
    houses_df = pd.read_csv("D:\\OneDevelopment\\Online Courses\\Data Visualization Analysis in "
                            "Python\\data\\kc_house_data.csv", parse_dates=["date"])
    print("Dataframe Info", houses_df.info())
    houses_df.sort_values("date", inplace=True)
    print("Dataset Span:", (houses_df["date"].iloc[len(houses_df.index)-1]-houses_df["date"].iloc[0]).days, "days")

    print("Most sales on a day:", houses_df["date"].value_counts().max())
    print(houses_df["date"].mode()[0])

    print(houses_df[houses_df["date"].dt.year == 2014].sort_values("date"))

    print(houses_df["date"].month.value_counts().head(1))

    one_year = houses_df["date"].between("2014-05-01", "2015-05-01").sort_values("date")
    one_year["date"].dt.month.value_counts().sort_index().plot()
    plt.show()
    pass


def section10():
    mat.stylesheets()
    mat.plotting_exercise(dataf.get_houses_example())
    pass


def section11():
    df = dataf.get_titanic_example()
    # grp.grouping_example(df, "sex")
    grp.aggregate_example(df, "age", "age", ["min", "max", "mean"])

    laliga = dataf.get_laliga_example()
    grp.grp_agg_exercise(laliga)


# Docs for pandas api: pandas.pydata.org
# Datasets acquired from kaggle.com
def main():
    # Section 1: Import and read DataFrames from Delimiter Separated Value files
    # get_dataframes()

    # Section 2: Basic Computations on Dataframes & Series
    # section2()

    # Section 3: Selecting Series & Dataframes & basic visualization
    # section3()

    # Section 4: Indexing and sorting Dataframes and Series
    # section4()

    # Section 5: Filtering
    # section5()

    # Section 6: Adding and Dropping Columns
    # section 6()

    # Section 7: Updating Values
    # section7()

    # Section 8: Working with types & NA Values
    # section8()

    # Section 9: Working with Dates & Times
    # section9()

    # Section 10: Matplotlib plots practice
    # section10()

    # Section 11: Grouping & Aggregating
    # section11()

    # Section 13: Seaborn
    sea.seaborn_example()
    pass


if __name__ == '__main__':
    main()
