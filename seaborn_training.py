import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reference: https://seaborn.pydata.org/tutorial.html#api-overview
# Data visualization lib built on top of matplotlib
# Provides a high level interface to make complex charts with even a single line of code
# Has very attractive styles for charts
# Works very well with Pandas & Numpy


def seaborn_example():
    # load dataset works exactly like read_csv, can pass args like parse_dates, etc
    # penguins = sns.load_dataset("penguins")
    tips = sns.load_dataset("tips")

    print(tips.info())
    sns.set_theme()
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", style="sex")

    lineplot_example()
    relplots_example()
    # Remember to use plt.show()
    plt.show()


def lineplot_example():
    # Default behaviour of lineplot is using the mean number of whatever you pass as the value for the lineplot
    # It also sorts the x axis. can use sort = False to disable that.
    # To disable the shadowy part around lines, use ci = False (Confidence Indicator)
    flights = sns.load_dataset("flights")
    print(flights)
    sns.lineplot(data=flights, y="passengers", x="year", estimator=sum)

    trips = sns.load_dataset("taxis")
    print(trips.info())
    sns.lineplot(data=trips, y="total", x="pickup", ci=False)


def relplots_example():
    tips = sns.load_dataset("tips")
    sns.relplot(data=tips, x="tip", y="total_bill", kind="scatter", col="sex", row="smoker")