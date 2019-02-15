from custom_utils.science.imports import *
from custom_utils.science import basics as sb

sb.use_mpl_latex_style()

u2 = sb.dataframe_from_csv("../data/u2.csv")
u3 = sb.dataframe_from_csv("../data/u3.csv")
u6 = sb.dataframe_from_csv("../data/u6.csv")


def plot_u2(show=False, save=False):

    fig = plt.figure(figsize=(3.7, 2.5))
    ax = fig.add_subplot(111)

    ax.plot(u2.U, u2.I_6cm * 1e3, "+", c="k", label="$d = \SI{6}{cm}$")
    ax.plot(u2.U, u2.I_2cm * 1e3, "+", c="grey", label="$d = \SI{2}{cm}$")

    ax.set_xlabel(r"$U[\si{V}]$")
    ax.set_ylabel(r"$I[\si{pA}]$")
    ax.legend()
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../fig/u2.pdf")

    plt.close(fig)


def plot_u6(show=False, save=False):

    fig = plt.figure(figsize=(4.2, 2.5))
    ax = fig.add_subplot(111)

    spline = sb.Spline(u6.U, u6.impuls)
    spline.set_smoothing_factor(90)

    ax.plot(*spline.curve(), ":", c="grey")
    ax.plot(u6.U, u6.impuls, "k+", label="naměřené hodnoty")

    ax.set_xlabel(r"$U[\si{V}]$")
    ax.set_ylabel(r"$U_i[\si{V}]$")
    ax.set_yscale("log")
    ax.legend()
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../fig/u6.pdf")

    plt.close(fig)


def table_u2():

    cp = [
        "U $U$ V 2.0".split(),
        "I_6cm $I_{\SI{6}{cm}}$ nA 1.4".split(),
        "I_2cm $I_{\SI{2}{cm}}$ nA 1.4".split(),
    ]

    sb.df_to_booktabs_table(u2, cp, "../tab/u2.tex")


def table_u3():

    cp = [
        "d $d$ cm 1.0".split(),
        "I $I$ nA 1.4".split(),
    ]

    sb.df_to_booktabs_table(u3, cp, "../tab/u3.tex")


def table_u6():

    cp = [
        "U $U$ V 4.0".split(),
        "impuls $U_i$ V 3.1".split()
    ]

    sb.df_to_booktabs_table(u6, cp, "../tab/u6.tex")
