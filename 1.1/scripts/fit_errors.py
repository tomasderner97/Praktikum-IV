from pandas import DataFrame
from scireputils.curve_fitting import FitCurve
from scireputils.plotting import matplotlib_use_latex_style

from project_wide import *

matplotlib_use_latex_style()


def f_fit2(N, a):
    return a / np.sqrt(N)


def get_errors():
    df = DataFrame()
    df["N"] = [50, 100, 200, 500, 1000, 1647]
    df["err"] = [0.36, 0.55, 0.34, 0.183, 0.137, 0.112]
    return df


def plot_fit_errors():
    fig, ax = plt.subplots(figsize=[6,3.5])

    df = get_errors()

    fit2 = FitCurve(f_fit2, df["N"], df["err"])

    ax.plot(*fit2.curve(), c="grey", label="fit")
    ax.plot(df["N"], df["err"], "kx", label="hodnoty")

    ax.set_xlabel("$N$")
    ax.set_ylabel("$s_{\\mu}$")
    ax.legend()

    fig.tight_layout()

    fig.savefig("../plots/fit_errors.pdf")

    return fig, ax, fit2
