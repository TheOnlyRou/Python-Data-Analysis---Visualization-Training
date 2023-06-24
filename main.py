import computations as comp
import dataframes as dataf
import series_columns as sc
import indices_sorting as ind
import filtering as filt
import modifying_columns as mdf


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

    # Section 6:
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
    pass


if __name__ == '__main__':
    main()
