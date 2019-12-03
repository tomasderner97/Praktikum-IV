import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from scireputils.curve_fitting import FitCurve, f_line
from scireputils.dataframes import dataframe_from_csv
from scireputils.plotting import matplotlib_use_latex_style
from uncertainties import ufloat

matplotlib_use_latex_style()


def Ux_to_x(Ux):
    return 21.2 * Ux + 1.9


def get_proud(file):
    return dataframe_from_csv(file,
                              sep=" ",
                              names=["sys_time", "delta_time", "x", "y"],
                              header=None)


def get_proud_0A():
    return get_proud("../data/proud_0A.txt")


def plot_fit_0A():
    fig, ax = plt.subplots()

    df = get_proud_0A().sort_values("x")
    df["x"] = Ux_to_x(df["x"])

    upper_y = 0.78
    lower_y = 0.43

    df_for_fit_left = df[4700:6000]
    df_for_fit_right = df[6800:7700]

    fit_left = FitCurve(f_line, df_for_fit_left["x"], df_for_fit_left["y"])
    fit_right = FitCurve(f_line, df_for_fit_right["x"], df_for_fit_right["y"])

    ax.plot(df["x"], df["y"], c="grey", lw=0.4, label="data")
    ax.plot(df["x"], f_line(df["x"], *fit_left.params), "k", label="fit přímkou", lw=0.8)
    ax.plot(df["x"], f_line(df["x"], *fit_right.params), "k", lw=0.8)

    upper_line = Line2D(
        [Ux_to_x(0.464), Ux_to_x(0.50)],
        [upper_y, upper_y],
        lw=0.8,
        linestyle="-.",
        c="k",
        label="odečtení $2p$"
    )
    ax.add_line(upper_line)

    lower_line = Line2D(
        [Ux_to_x(0.464 - 0.02), Ux_to_x(0.50 + 0.02)],
        [lower_y, lower_y],
        lw=0.8,
        linestyle="--",
        c="k",
        label="odečtení $2D$"
    )
    ax.add_line(lower_line)

    ax.text(12.12, lower_y - 0.01, "$2D$", verticalalignment="top", horizontalalignment="center")
    ax.text(12.12, upper_y - 0.01, "$2p$", verticalalignment="top", horizontalalignment="center")

    ax.set_xlabel("$x[\\si{mm}]$")
    ax.set_ylabel("$y$")

    ax.set_ylim(0.3, 1)
    ax.set_xlim(Ux_to_x(0.35), Ux_to_x(0.6))

    ax.legend()

    plt.tight_layout()
    plt.savefig("../plots/0A_fit.pdf")


tesla = {
    0.0: 0,
    0.26: 0.18,
    0.38: 0.28,
    0.51: 0.39,
    0.77: 0.57,
    0.98: 0.67,

}


def plot_proud():
    fig, axs = plt.subplots(6, 1, figsize=[6, 6], sharex=True)

    for ax, current in zip(axs, "0 0.26 0.38 0.51 0.77 0.98".split()):
        df = get_proud(f"../data/proud_{current}A.txt").sort_values("x")
        df["x"] = Ux_to_x(df["x"])

        ax.plot(df["x"], df["y"], "k", label=f"$B = \\SI{{{tesla[float(current)]}}}{{mT}}$")
        ax.set_ylabel("$y$")
        ax.set_xlim(Ux_to_x(0.25), Ux_to_x(0.65))
        ax.legend(loc="lower right")

    axs[5].set_xlabel("$x[\\si{mm}]$")

    fig.tight_layout()

    fig.savefig("../plots/curves.pdf")

    return fig, axs


p = (12.41 - 11.83) / 2  # chyba 0.03
D = (12.82 - 11.38) / 2

C = (D ** 4 - p ** 4 / 5) / (D ** 2 - p ** 2 / 3)

if __name__ == '__main__':
    plot_fit_0A()
    plt.show()
