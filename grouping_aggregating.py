import pandas as pd
import matplotlib.pyplot as plt


def grouping_example(df, col):

    grouped = df.groupby(col)

    print("Number of Groups", grouped.ngroups)

    print(grouped.get_group("male"))

    for name, group in grouped:
        print(f"Name: {name} Group:\n {group}")

    print(grouped["age"].max())
    print(grouped["age"].min())
    print(grouped["age"].mean())


def aggregate_example(df, col1, col2, functions: list):
    # Run functions on the col2 selected

    # can also write this like that
    df[col1].replace(["?"], [None], inplace=True)

    df[col1] = df[col1].astype("float")
    print(df["age"].value_counts())
    print(df.info())
    print(df.groupby(col1)[col2].agg(functions))
    print("_____________________________________________________")
    print(df.groupby(col1).agg({"age": ["min", "max"], "pclass": "mean"}))

    # Can also use user defined values
    print(df.groupby(col1)[col1].agg(range_of))

    # Can also name columns of the aggregate
    print(df.groupby(col1).agg(min_age=("age", "min"), max_age=("age", "max")))


def range_of(x):
    return x.max() - x.min()


def total(x):
    return x.sum()


def on_target(x):
    return x.sum()


def grp_agg_exercise(df):
    print(df.info())
    # Find team with most Red cards
    print("Teams with Most Red Cards")
    print(df.groupby("Team")["Red Cards"].sum().sort_values(ascending=False).head(5))

    print("Average Num of Long passes Made by each Position")
    print(df.groupby("Position")["Long passes"].mean().sort_values())

    df["Shirt number"] = df["Shirt number"].fillna(-1)
    df["Shirt number"] = df["Shirt number"].astype("int64")
    print(df.groupby("Shirt number")["Goals scored"].sum().sort_values(ascending=False).head(10))

    # Total goals scored vs Total shots on Target
    shots_filter = df.groupby("Team").agg(total_goals=("Goals scored", total), total_shots=("Shots", total),
                                           on_target=("Shots on target", on_target))\
        .sort_values(ascending=False, by=["total_goals", "on_target"])

    shots_accuracy = shots_filter["on_target"] / shots_filter["total_shots"]
    goals_accuracy = shots_filter["total_goals"] / shots_filter["total_shots"]

    shots_filter["Shots Accuracy"] = shots_accuracy
    shots_filter["Shot to Goal Accuracy"] = goals_accuracy

    most_shots_accuracy = shots_filter.sort_values(by="Shots Accuracy", ascending=False).head(5)["Shots Accuracy"].sort_values()
    least_shots_accuracy = shots_filter.sort_values(by="Shots Accuracy", ascending=False).tail(5)["Shots Accuracy"].sort_values()
    most_goals_accuracy = shots_filter.sort_values(by="Shots Accuracy", ascending=False).head(5)["Shot to Goal Accuracy"].sort_values()
    least_goals_accuracy = shots_filter.sort_values(by="Shots Accuracy", ascending=False).tail(5)["Shot to Goal Accuracy"].sort_values()
    plt.figure()
    plt.suptitle("Shot accuracy in LaLiga")
    plt.subplot(1, 2, 1)

    plt.title("Most Accurate Teams")
    plt.barh(most_shots_accuracy.index.values, most_shots_accuracy, label = "Shots on target ratio")
    plt.barh(most_goals_accuracy.index.values, most_goals_accuracy, label = "Shots to goals ratio")
    plt.xlabel("On Target Percentage")
    plt.ylabel("Teams")
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.title("Least Accurate Teams")
    plt.barh(least_shots_accuracy.index.values, least_shots_accuracy, label="Shots on target ratio")
    plt.barh(least_goals_accuracy.index.values, least_goals_accuracy, label="Shots to goals ratio")
    plt.xlabel("On Target Percentage")
    plt.ylabel("Teams")
    plt.legend()
    plt.show()






