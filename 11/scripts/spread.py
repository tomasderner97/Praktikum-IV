import matplotlib.pyplot as plt
from scireputils.curve_fitting import FitCurve, f_line
from scireputils.dataframes import dataframe_from_csv
from scireputils.plotting import matplotlib_use_latex_style

from curves import C

matplotlib_use_latex_style()


def grad_B(B):
    return 0.968 * B / 2.5


def get_spread():
    df = dataframe_from_csv("../data/spread.csv")
    df["dx"] = df["dU"] * 21.2
    df["q"] = 3 * df["dx"] / 2 - C / (df["dx"] / 2)
    df["grad_B"] = grad_B(df["B"])
    return df


def plot_fit():
    fig, ax = plt.subplots()

    df = get_spread()[1:]

    fit = FitCurve(lambda x, a: a*x, df["q"], df["grad_B"])

    ax.plot(*fit.curve(), c="grey", label="fit přímkou")
    ax.plot(df["q"], df["grad_B"], "kx", label="data")

    ax.set_xlabel("$q[\\si{mm}]$")
    ax.set_ylabel("$\\frac{\\partial B}{\\partial x} [\\si{\\tesla\\per\\milli\\metre}]$")

    ax.legend()

    fig.tight_layout()
    fig.savefig("../plots/spread.pdf")

    return fig, ax, fit
