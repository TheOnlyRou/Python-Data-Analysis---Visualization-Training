import computations as comp
import dataframes as dataf
import series_columns as sc
import indices_sorting as ind


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
    sc.exercise(dataf.get_bestsellers_example(), column_name='Author', ex= 1)
    sc.exercise(dataf.get_bestsellers_example(), columns=['Name', 'User Rating'], ex=1 )
    # Part 2 Exercise
    sc.exercise(dataf.get_bestsellers_example(), column_name='Genre', ex=2)
    sc.exercise(dataf.get_bestsellers_example(), column_name='Author', ex=2)
    sc.exercise(dataf.get_bestsellers_example(), column_name='Price', ex=2)
    # Part 3
    sc.exercise(dataf.get_bestsellers_example(), column_name='Name', columns=['Author', 'User Rating'], ex=3)
    # Part 4
    sc.exercise(dataf.get_bestsellers_example(), column_name='Genre', ex=4, plot_type = "pie")
    sc.exercise(dataf.get_bestsellers_example(), column_name='Author', plot_type = 'barh', ex=4)
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

    pass


if __name__ == '__main__':
    main()
