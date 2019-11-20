import pandas
from scireputils.curve_fitting import FitCurve, f_line
from scireputils.dataframes import dataframe_from_csv
import matplotlib.pyplot as plt
from scireputils.plotting import matplotlib_use_latex_style

from project_wide import calibration

matplotlib_use_latex_style()


def get_lines():
    df = dataframe_from_csv("../data/lines.csv")

    for col in list(df.columns):
        df[f"lambda_{col}"] = calibration(df[col])
    return df


def get_hydrogen():
    df = pandas.DataFrame()
    df["lambda"] = [656.9, 486.4, 434.2]
    df["lambda"] = df["lambda"] * 1e-9
    df["1/lambda"] = 1 / df["lambda"]
    df["n"] = [3, 4, 5]
    df["parenthesis"] = 1 / 4 - 1 / df["n"] ** 2
    return df


def plot_hydrogen():
    fig, ax = plt.subplots()

    df = get_hydrogen()

    fit = FitCurve(lambda x, a: f_line(x, a, 0), df["parenthesis"], df["1/lambda"])
    print("params", fit.params)
    print("errors", fit.errors)

    ax.plot(*fit.curve(overrun=0.05), c="gray", label="$f(x) = Rx$")
    ax.plot(df["parenthesis"], df["1/lambda"], "kx", label="hodnoty")

    ax.set_xlabel(r"$\left( \frac{1}{4} - \frac{1}{n^2} \right)$")
    ax.set_ylabel(r"$\frac{1}{\lambda} [\si{\per\metre}]$")
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    ax.autoscale(axis="x", tight=True)
    ax.legend()

    fig.tight_layout()

    fig.savefig("../plots/rydberg.pdf")

    return fig, ax
