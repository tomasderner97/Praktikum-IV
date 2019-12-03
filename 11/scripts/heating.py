from scireputils.dataframes import dataframe_from_csv
import matplotlib.pyplot as plt
from scireputils.plotting import matplotlib_use_latex_style

matplotlib_use_latex_style()


def get_heating():
    return dataframe_from_csv("../data/heating.csv")


def plot_heating():
    df = get_heating()
    fig, ax = plt.subplots(figsize=[6, 2.5])

    ax.plot(df["T"], df["U"], "kx", label="Naměřené hodnoty")
    ax.set_xlabel("$t [\\si{\\celsius}]$")
    ax.set_ylabel("$U [\\si{V}]$")

    ax.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))

    fig.tight_layout()

    fig.savefig("../plots/heating.pdf")
