from custom_utils.science.imports import *
from custom_utils.science import basics as sb

sb.use_mpl_latex_style()

MI_0 = 4e-7 * sp.pi
N = 630
RO_0 = 75e-3
R_A = uf(5, 0.05) * 1e-3
R_K = uf(0.19, 0.01) * 1e-3


def plot_u1(f, amps, show=False, save=False):

    fig = plt.figure(figsize=(3, 1.85))
    ax = fig.add_subplot(111)

    df = sb.dataframe_from_csv(f"../data/raw/{f}.txt", sep=" ", header=None)

    ax.plot(df[0], df[1], "k")

    ax.set_xlabel(r"$U$ [V]")
    ax.set_ylabel(r"$I$ [A]")
    # ax.legend()
    ax.set_title(f"$I_{{mag}} = \SI{{{amps}}}{{A}}$")
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        f_ = f.replace(".", "")
        fig.savefig(f"../fig/u1_{f_}.pdf")

    plt.close(fig)


files_amps = {
    "0.5A_5Vs": 0.5076,
    "0.75A_5Vs": 0.7584,
    "1A_5Vs": 0.996,
    "1.2A_5Vs": 1.202,
    "1.4A_5Vs": 1.405,
    "1.6A_5Vs": 1.602,
    "1.7A_5Vs": 1.701,
    "1.8A_5Vs": 1.791,
    "1.9A_5Vs": 1.889,
    "2A_5Vs": 2.01
}


def make_u1_plots():

    for f, a in files_amps.items():

        plot_u1(f, a, False, True)


u2 = sb.dataframe_from_csv("../data/u2.csv")
u2 = u2.sort_values("I_mag")


def plot_u2(show=False, save=False):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    fit = sb.FitCurve(sb.f_line, u2.I_mag**2, u2.U_kr)

    ax.plot(*fit.curve(), ":", c="gray", label="lineární fit")
    ax.plot(u2.I_mag**2, u2.U_kr, "kx", label="kritická napětí")

    ax.set_xlabel(r"$ I_{mag}^2 [\si{\ampere\squared}] $")
    ax.set_ylabel(r"$ U_{kr}$ [V]")
    ax.legend()
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../fig/u2.pdf")

    plt.close(fig)

    return fit


u2_fit = plot_u2()

slope = sb.uf(u2_fit.params[0], u2_fit.errors[0] + 1)

e_me = slope / (
    8 * MI_0**2 * N**2 * R_A**2 * (1 - R_K**2 / R_A**2)**2 / (125 * RO_0**2)
)

print(f"e/m_e = {e_me}")


def table_u2():

    cp = [
        ["I_mag", "$I_{mag}$", "A", "1.3"],
        ["U_kr", "$U_{kr}$", "V", "3.1"],
        ["s_U_kr", "$\sigma_{U_{kr}}$", "V", "1.1"]
    ]

    sb.df_to_booktabs_table(u2, cp, "../tab/u2.tex")


u3 = sb.dataframe_from_csv("../data/raw/0.5A_5Vs.txt", sep=" ", header=None)
u3.rename({0: "U", 1: 0.5}, axis=1, inplace=True)

names = [
    0.5,
    0.75,
    0.97,
    0.98,
    0.99,
    1,
    1.01,
    1.02,
    1.03,
    1.2,
    1.4,
    1.6,
    1.7,
    1.8,
    1.9,
    2

]

for n in names:

    df = sb.dataframe_from_csv(f"../data/raw/{n}A_5Vs.txt", sep=" ", header=None)
    u3[n] = df[1].values

u3 = u3.drop("U", 1)


def plot_u3(show=False, save=False):

    fig = plt.figure(figsize=(6, 3))
    ax = fig.add_subplot(111)

    B = u3.T.index.values * N * 8 * MI_0 / (5 * sp.sqrt(5) * RO_0)
    ax.plot(B, u3.T[7], "kx", label="$U = \SI{30}{V}$")

    ax.set_xlabel(r"$B$ [H]")
    ax.set_ylabel(r"$I$ [A]")
    ax.legend()
    ax.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))
    ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../fig/u3.pdf")

    plt.close(fig)
