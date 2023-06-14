import pandas as pd
import computations as comp
import dataframes as dataf


def get_dataframes():
    dataf.get_bestsellers_example()
    dataf.get_everest_example()
    dataf.get_movietitles_example()
    dataf.get_houses_example()
    dataf.get_titanic_example()
    dataf.get_netflix_example()


def run_computations():
    comp.compute_basic(dataf.get_bestsellers_example())
    comp.compute_basic(dataf.get_everest_example())
    comp.compute_basic(dataf.get_movietitles_example())
    comp.compute_basic(dataf.get_houses_example())
    comp.compute_basic(dataf.get_titanic_example())
    comp.compute_basic(dataf.get_netflix_example())


def main():
    # Section 1: Import and read DataFrames from Delimiter Separated Value files
    # get_dataframes()

    # Section 2: Basic Computations
    #run_computations()
    comp.exercise(dataf.get_bestsellers_example())


if __name__ == '__main__':
    main()

