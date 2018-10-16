from custom_utils.science.imports import *
from custom_utils.science import basics as sb

sb.use_mpl_latex_style()

u3 = sb.dataframe_from_csv("../data/u3.csv")

u3.s_a_i = u3.s_a_i * u3.a_i / 100
u3.s_a_s = u3.s_a_s * u3.a_s / 100
u3.E0 *= 1e9


def f_a(sqrt_E0, resolution, c):

    return resolution * sqrt_E0 + c


def plot_u3_i(show=False, save=False):

    fig = plt.figure(figsize=(3, 2))
    ax = fig.add_subplot(111)

    ax.plot(sp.sqrt(u3.E0), u3.a_i, "kx", label="$a_i(E_0)$")

    ax.set_xlabel(r"$\sqrt{E_0}[eV]$")
    ax.set_ylabel(r"$a_i$")
    ax.ticklabel_format(style="sci", axis="x", scilimits=(0, 0))
    ax.legend()
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../fig/u3_i2.pdf")


def plot_u3_s(show=False, save=False):

    fig = plt.figure(figsize=(3, 2))
    ax = fig.add_subplot(111)

    ax.plot(sp.sqrt(u3.E0), u3.a_s, "kx", label="$a_s(E_0)$")

    ax.set_xlabel(r"$\sqrt{E_0}[eV]$")
    ax.set_ylabel(r"$a_s$")
    ax.ticklabel_format(style="sci", axis="x", scilimits=(0, 0))
    ax.legend()
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../fig/u3_s2.pdf")


cp = [
    ["E0", "$E_0$", "eV", "1.1e1"],
    ["a_i", "$a_i$", "", "1.2"],
    ["a_s", "$a_s$", "", "2.2"],
]
sb.df_to_booktabs_table(u3, cp, "../tab/u3.tex")
