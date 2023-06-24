import pandas as pd


def get_houses_example():
    # id` - house's unique id"
    # date` - sale date",
    # price` - sale price",
    # bedrooms` - number of bedrooms",
    # bathrooms` - numbers of bathrooms",
    # sqft_living` - living space square footage ",
    # sqft_lot` - total lot square footage",
    # floors` - numbers of floors",
    # waterfront` - is the house waterfront (1) or not (0)",
    # view` - rating from 0 to 4 of how good the view from the house is",
    # condition` - rating from 1 (poor) to 5 (very good) of the condition of the house",
    # grade` - rating from 1-13 representing the construction quality of improvements. 1-3 Falls short of minimum
    #               building standards (cabins, etc.) 7 is avg grade, 11-13 have high-quality design & construction",
    # sqft_above` - square footage of the interior that is above ground level",
    # sqft_basement` - square footage of the interior that is below ground level",
    # yr_built` - year the house was initially built",
    # yr_renovated` - The year of the house’s last renovation (if any)",
    # zipcode` - zipcode that the house is located in",
    # lat` - the property's latitude",
    # long` - the property's longitude",
    # sqft_living15` - average interior space square footage of the nearest 15 neighbors",
    # sqft_lot15` - average lot square footage of the nearest 15 neighbors"
    houses_df = pd.read_csv("D:\\OneDevelopment\\Online Courses\\Data Visualization Analysis in "
                            "Python\\data\\kc_house_data.csv")
    return houses_df


def get_states_example():
    states_df = pd.read_csv("D:\\OneDevelopment\\Online Courses\\Data Visualization Analysis in "
                            "Python\\data\\states.csv")
    return states_df


def get_netflix_example():
    # Reading a csv file with a different separator and defiing an existing index column in the csv file
    netflix_df = pd.read_csv("D:\\OneDevelopment\\Online Courses\\Data Visualization Analysis in "
                             "Python\\data\\netflix_titles.csv", sep="|", index_col=0)
    return netflix_df


def nst_est_example():
    # Reading a csv file with header names that we want to replace, so we set header=0, then provide the new names in
    # names as a list
    nst_est_df = pd.read_csv("D:\\OneDevelopment\\Online Courses\\Data Visualization Analysis in "
                             "Python\\data\\nst-est2020.csv", names=['sumlev', 'region', 'division', 'state', 'name',
                                                                     'census2010pop', 'estimatesbase2010',
                                                                     'popestimate2010', 'popestimate2011',
                                                                     'popestimate2012', 'popestimate2013',
                                                                     'popestimate2014', 'popestimate2015',
                                                                     'popestimate2016', 'popestimate2017',
                                                                     'popestimate2018', 'popestimate2019',
                                                                     'popestimate042020', 'popestimate2020'], header=0)


def get_titanic_example():
    # Import the titanic dataset
    titanic_df = pd.read_csv("D:\\OneDevelopment\\Online Courses\\Data Visualization Analysis in "
                             "Python\\data\\titanic.csv")
    return titanic_df


def get_bestsellers_example():
    bestsellers_df = pd.read_csv("D:\\OneDevelopment\\Online Courses\\Data Visualization Analysis in "
                                 "Python\\data\\bestsellers.csv")
    return bestsellers_df


def get_bitcoin_example():
    bitcoins_df = pd.read_csv("D:\\OneDevelopment\\Online Courses\\Data Visualization Analysis in "
                              "Python\\data\\coin_Bitcoin.csv")
    return bitcoins_df


def get_countries_example():
    countries_df = pd.read_csv("D:\\OneDevelopment\\Online Courses\\Data Visualization Analysis in "
                              "Python\\data\\countries of the world.csv")
    return countries_df


def get_tweets_example():
    tweets_df = pd.read_csv("D:\\OneDevelopment\\Online Courses\\Data Visualization Analysis in "
                              "Python\\data\\JoeBidenTweets.csv")
    return tweets_df


def get_pokemon_example():
    pokemon_df = pd.read_csv("D:\\OneDevelopment\\Online Courses\\Data Visualization Analysis in "
                              "Python\\data\\Pokemon.csv")
    return pokemon_df

def get_happiness_example():
    happiness_df = pd.read_csv("D:\\OneDevelopment\\Online Courses\\Data Visualization Analysis in "
                              "Python\\data\\world-happiness-report-2021.csv")
    return happiness_df


def get_everest_example():
    everest_df = pd.read_csv("D:\\OneDevelopment\\Online Courses\\Data Visualization Analysis in "
                             "Python\\data\\mount_everest_deaths.csv", index_col=0)
    return everest_df


def get_movietitles_example():
    # Reading a delimiter separated value file with a difference separator: \t
    names = ["id", "title", "year", "imdb_rating", "imdb_id", "genres"]
    movie_titles_df = pd.read_csv("D:\\OneDevelopment\\Online Courses\\Data Visualization Analysis in "
                                  "Python\\data\\movie_titles.tsv", sep="\t", names=names)
    return movie_titles_df


def exercise():
    print(get_houses_example().shape)
    print(get_houses_example().size)

    # creates a new dataframe with n number of rows from the head (start) of the dataframe
    print(get_houses_example().head(2))
    # creates a new dataframe with n number of rows from the tail (end) of the dataframe
    print(get_houses_example().tail(2))

    # Displays dataframe column information (Non-null, Datatype)
    print(get_houses_example().info())

    # Displays only datatype information about columns in the dataframe
    print(get_houses_example().dtypes)

    print(get_movietitles_example().tail(7))

    print(get_everest_example().shape)
    print(get_everest_example().info())
    # Columns 0 & 1 have 0 null values
    # Expedition column has most null values (39)

    print(get_bestsellers_example().shape)
    print(get_bestsellers_example().size)
    print(get_bestsellers_example().info())
    print(get_bestsellers_example().dtypes)
    print(get_bestsellers_example().head())
    print(get_bestsellers_example().head(19))
    print(get_bestsellers_example().tail())
    print(get_bestsellers_example().tail(2))
    # 550 rows, 7 columns
    # No missing values
    # Float64
    # 3 Integer Columns

    # pclass` - Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)",
    # survived` - Survival (0 = No; 1 = Yes)",
    # name` - Name",
    # sex` - Sex",
    # age` - Age",
    # sibsp` - Number of Siblings/Spouses Aboard",
    # parch` - Number of Parents/Children Aboard",
    # ticket` - Ticket Number",
    # fare` - Passenger Fare",
    # cabin` - Cabin",
    # embarked` - Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)",
    # boat` - Lifeboat (if survived)",
    # body` - Body number (if did not survive and body was recovered)",
    # home.dest` - Home/Destination"
    print(get_titanic_example().head(2))
    print(get_titanic_example().tail(2))
    print(get_titanic_example().dtypes)

    print(get_netflix_example().head(2))
    print(get_netflix_example().tail(2))
    print(get_netflix_example().dtypes)
