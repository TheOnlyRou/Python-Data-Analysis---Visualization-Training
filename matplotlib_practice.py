import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nums = np.arange(5)
mul = nums * nums
add = nums + nums

# Reference: https://matplotlib.org/stable/plot_types/basic/plot.html
def example_plots():
    # Passing only y if you only provide one vector
    plt.plot([2, 4, 6, 8, 10])
    plt.show()
    salaries = [55000, 65000, 75000, 850000, 950000]
    ages = [20, 25, 30, 40, 45]

    # You can also use numpy series, pandas series, dataframes, etc
    plt.plot(ages, salaries)
    plt.show()


def figures_exploration():
    # Creates a new figure, sets it as active so anything that gets plotted after this line gets plotted on same figure
    plt.figure()
    plt.title("Test Figure") # Use plt.suptitle() if you are using subplots
    plt.plot(nums, nums)
    plt.xlabel("Age")
    plt.ylabel("Money")
    plt.plot(nums, nums*nums)
    plt.plot(nums, nums **3)

    # To plot each one in a separate figure, you can use the following code:
    # plt.figure()
    # plt.plot(nums, nums)
    # plt.figure()
    # plt.plot(nums, nums*nums)
    # plt.figure()
    # plt.plot(nums, nums * nums * nums)

    # To specify what ticks are on the x and y axis, you can also use
    # plt.xticks([20,30,40,...]) or plt.yticks([100, 200, 300, ...])
    # You can also set the labels for the ticks you use
    # plot.xticks([20,30,40,...], labels = ["20k","30k","40k",...])

    # To control start and stop points use xlim and ylim
    # ex: plt.xlim(startlim, endlim), plt.ylim(startlim, endlim)

    # To label the plots on a certain figure, you can use plt.legend()
    # You can also add paramters shadow or border. Refer to reference for more details on styling the legend
    # However, you have to make sure that every plt.plot has a label parameter passed to it.
    plt.show()


def subplots_example():
    plt.figure()
    plt.suptitle("Test Figure")

    plt.subplot(1,3,1)
    ax = plt.plot(nums, nums)
    plt.title("X")
    plt.xlabel("X Label")
    plt.ylabel("Y Label")

    plt.subplot(1,3,2)
    plt.plot(nums, nums * nums, sharey = ax) # sharey used to share the same axis scale of Y as the axis ax
    plt.title("X Squared")
    plt.xlabel("X Label")
    plt.ylabel("Y Label")

    plt.subplot(1,3,3)
    plt.title("X Cubic")
    plt.xlabel("X Label")
    plt.ylabel("Y Label")
    plt.plot(nums, nums ** 3, sharey = ax)


def control_figure_size():
    nums = np.arange(5)

    # Width * Height & dpi (dots per inch)
    plt.figure((20, 6), dpi=10)
    plt.plot()


def stylesheets():
    print(plt.style.available)
    # To use a stylesheet, use
    # plt.style.use("stylesheet name")

def plot_with_style():
    # Color par: c or color
    plt.plot(nums, nums**3, c="#ff2122")
    # Line width par: lw or linewidth
    plt.plot(nums, nums ** 2,  lw=2.0)
    # Linestyle par: ls or linestyle
    plt.plot(nums, nums ** 3, linestyle=".-")


def plotting_exercise(df):
    print(df.info())
    df["date"] = pd.to_datetime(df["date"])
    plt.figure(figsize = (10, 4), dpi = 200)
    plt.style.use("fivethirtyeight")

    plt.subplot(1,2,1)
    sales_day = df["date"].dt.dayofweek.value_counts().sort_index()

    plt.title("Sales by Week Day")

    # Can also use sales_day.index.values
    plt.bar(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], sales_day)

    plt.subplot(1, 2, 2)
    sales_month = df["date"].dt.month.value_counts().sort_index()
    plt.plot(sales_month, lw=2.0)
    plt.ylabel("Home Sales")
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12])

    plt.title("Sales by Month")
    plt.show()




