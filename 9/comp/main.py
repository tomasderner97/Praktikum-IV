from custom_utils.science.imports import *
from custom_utils.science import basics as sb
from scipy.constants import c

u1 = sb.dataframe_from_csv("../data/u1.csv")
u3 = sb.dataframe_from_csv("../data/data_planck.csv")

sb.use_mpl_latex_style()


def plot_u1(show=False, save=False):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(u1.U, u1.GKV, "k", label="závislost vakuové fotonky GKV")
    ax.plot(u1.U, u1.GKE, c="grey", label="závislost plynové fotonky GKE")

    ax.set_xlabel(r"U[V]")
    ax.set_ylabel(r"I[nA]")
    ax.legend()
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../plot/u1.pdf")


def plot_u3_578(show=False, save=False):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    dropped = u3.I578.dropna()
    y = sp.zeros((dropped.size)) + dropped.min()

    lower = 11
    upper = 16
    fit = sb.FitCurve(sb.f_line, u3.U[lower:upper], u3.I578[lower:upper])

    ax.plot(u3.U[:dropped.size], y, c="grey", label="Nasycená hodnota proudu")
    ax.plot(u3.U, u3.I578, "k", label="Naměřená závislost")
    ax.plot(*fit.curve(overrun=(0.7)),
            c="red",
            label=r"Lineární fit v oblasti $U = \num{0.55} - \SI{0.75}{V}$")

    ax.set_xlabel(r"U[V]")
    ax.set_ylabel(r"I[nA]")
    ax.legend()
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../plot/u3_578.pdf")


def plot_u3_546(show=False, save=False):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    dropped = u3.I546.dropna()
    y = sp.zeros((dropped.size)) + dropped.min()

    lower = 14
    upper = 19
    fit = sb.FitCurve(sb.f_line, u3.U[lower:upper], u3.I546[lower:upper])

    ax.plot(u3.U[:dropped.size], y, c="grey", label="Nasycená hodnota proudu")
    ax.plot(u3.U, u3.I546, "k", label="Naměřená závislost")
    ax.plot(*fit.curve(overrun=(0.7)),
            c="red",
            label=r"Lineární fit v oblasti $U = \num{0.70} - \SI{0.90}{V}$")

    ax.set_xlabel(r"U[V]")
    ax.set_ylabel(r"I[nA]")
    ax.legend()
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../plot/u3_546.pdf")


def plot_u3_436(show=False, save=False):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    dropped = u3.I436.dropna()
    y = sp.zeros((dropped.size)) + dropped.min()

    lower = 21
    upper = 26
    fit = sb.FitCurve(sb.f_line, u3.U[lower:upper], u3.I436[lower:upper])

    ax.plot(u3.U[:dropped.size], y, c="grey", label="Nasycená hodnota proudu")
    ax.plot(u3.U, u3.I436, "k", label="Naměřená závislost")
    ax.plot(*fit.curve(overrun=(1.4)),
            c="red",
            label=r"Lineární fit v oblasti $U = \num{1.05} - \SI{1.25}{V}$")

    ax.set_xlabel(r"U[V]")
    ax.set_ylabel(r"I[nA]")
    ax.legend()
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../plot/u3_436.pdf")


def plot_u3_405(show=False, save=False):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    dropped = u3.I405.dropna()
    y = sp.zeros((dropped.size)) + dropped.min()

    lower = 22
    upper = 26
    fit = sb.FitCurve(sb.f_line, u3.U[lower:upper], u3.I405[lower:upper])

    ax.plot(u3.U[:dropped.size], y, c="grey", label="Nasycená hodnota proudu")
    ax.plot(u3.U, u3.I405, "k", label="Naměřená závislost")
    ax.plot(*fit.curve(overrun=(2)),
            c="red",
            label=r"Lineární fit v oblasti $U = \num{1.10} - \SI{1.30}{V}$")

    ax.set_xlabel(r"U[V]")
    ax.set_ylabel(r"I[nA]")
    ax.legend()
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../plot/u3_405.pdf")


def plot_u3_365(show=False, save=False):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    dropped = u3.I365.dropna()
    y = sp.zeros((dropped.size)) - 0.039

    lower = 27
    upper = 32
    fit = sb.FitCurve(sb.f_line, u3.U[lower:upper], u3.I365[lower:upper])

    ax.plot(u3.U[:dropped.size], y, c="grey", label="Nasycená hodnota proudu")
    ax.plot(u3.U, u3.I365, "k", label="Naměřená závislost")
    ax.plot(*fit.curve(overrun=(1.8)),
            c="red",
            label=r"Lineární fit v oblasti $U = \num{1.35} - \SI{1.55}{V}$")

    ax.set_xlabel(r"U[V]")
    ax.set_ylabel(r"I[nA]")
    ax.legend()
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../plot/u3_365.pdf")


V = {
    c / 365e-9: 1.89,
    c / 405e-9: 1.53,
    c / 436e-9: 1.50,
    c / 546e-9: 1.02,
    c / 578e-9: 0.88
}


def plot_planck(show=False, save=False):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    fit = sb.FitCurve(sb.f_line, list(V.keys()), list(V.values()), sigma=0.1)

    ax.plot(*fit.curve(), ":", c="grey", label="Lineární fit")
    ax.plot(V.keys(), V.values(), "kx", label="Spočtené hodnoty $U_0$")

    ax.set_xlabel(r"$\nu[\si{\per\second}]$")
    ax.set_ylabel(r"$U_0[V]$")
    ax.legend()
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../plot/planck.pdf")

    return fit
