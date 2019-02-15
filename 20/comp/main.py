from custom_utils.science.imports import *
from custom_utils.science import basics as sb
from scipy.constants import h

co = sb.dataframe_from_csv("../data/DERNER_CO.PRN", sep=" ", header=None)


def plot_co(show=False, save=False):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.plot(co[0], co[1], "k", lw=0.5)

    ax.set_xlabel(r"$\nu[\si{\per\centi\metre}]$")
    ax.set_ylabel(r"Transmitance")
    # ax.legend()
    ax.autoscale(True, "x", True)
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../fig/co.pdf")

    plt.close(fig)


u1 = sb.dataframe_from_csv("../data/Tomas_Derner_CO.csv")
u1 = pd.DataFrame({"Wavenumber": u1.Wavenumber.values})

u1_p = u1[:19]
u1_p = u1_p[::-1].reset_index(drop=True)
u1_p.set_index(u1_p.index.values + 1, inplace=True)
u1_r = u1[19:].reset_index(drop=True)
u1_p = u1_p * 1e2
u1_r = u1_r * 1e2

y_df = u1_r - u1_p
y = y_df.Wavenumber.values / (2 * y_df.index.values + 1)

x = (2 * y_df.index.values + 1)**2


def plot_u1_1(show=False, save=False):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    fit = sb.FitCurve(sb.f_line, x[1:-1], y[1:-1])

    ax.plot(*fit.curve(), ":", c="grey")
    ax.plot(x, y, "kx", label="hodnoty")

    ax.set_xlabel(r"x label")
    ax.set_ylabel(r"y label")
    ax.legend()
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../fig/u1_1.pdf")

    plt.close(fig)

    return fit


fit = plot_u1_1()
a = fit.params[0]
D_1 = -a / h
c = fit.params[1]
B_1 = (c / h + 3 * D_1) / 2


u3 = sb.dataframe_from_csv("../data/DERNER_VZDUCH.PRN", sep=" ", header=None)


def plot_u3(show=False, save=False):

    fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(6, 4))

    df = u3[(600 <= u3[0]) & (u3[0] <= 720)]
    ax1.plot(df[0], df[1], "k", lw=0.5)
    ax1.set_xlabel(r"$\nu[\si{\per\centi\metre}]$")
    ax1.set_ylabel(r"Transmitance")
    ax1.set_ylim(0.017, 0.031)
    ax1.autoscale(True, "x", True)

    df = u3[(2230 <= u3[0]) & (u3[0] <= 2400)]
    ax2.plot(df[0], df[1], "k", lw=0.5)
    ax2.set_xlabel(r"$\nu[\si{\per\centi\metre}]$")
    ax2.set_ylabel(r"Transmitance")
    ax2.autoscale(True, "x", True)

    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../fig/u3.pdf")

    plt.close(fig)
