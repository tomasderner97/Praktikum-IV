from custom_utils.science.imports import *
from custom_utils.science import basics as sb
from custom_utils.math.uncertainty import up_function

u3 = sb.dataframe_from_csv("../data/u3.csv")


def plot_u3(show=False, save=False):

    fig = plt.figure()
    ax = fig.add_subplot(111)

    fit40 = sb.FitCurve(sb.f_line, u3.I_40**2, u3.U_c)
    ax.plot(*fit40.curve(), ":", c="grey")
    ax.plot(u3.I_40**2, u3.U_c, "x", c="grey", label="$r = \SI{20}{mm}$")

    fit60 = sb.FitCurve(sb.f_line, u3.I_60**2, u3.U_c)
    ax.plot(*fit60.curve(), ":", c="C3")
    ax.plot(u3.I_60**2, u3.U_c, "x", c="C3", label="$r = \SI{30}{mm}$")

    fit80 = sb.FitCurve(sb.f_line, u3.I_80**2, u3.U_c)
    ax.plot(*fit80.curve(), ":", c="C1")
    ax.plot(u3.I_80**2, u3.U_c, "x", c="C1", label="$r = \SI{40}{mm}$")

    fit100 = sb.FitCurve(sb.f_line, u3.I_100**2, u3.U_c)
    ax.plot(*fit100.curve(), ":", c="C0")
    ax.plot(u3.I_100**2, u3.U_c, "x", c="C0", label="$r = \SI{50}{mm}$")

    ax.set_xlabel(r"$I_{mag}^2$ [A]")
    ax.set_ylabel(r"$U_c$ [V]")

    ax.legend()
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../fig/u3.pdf")

    plt.close(fig)

    return fit40, fit60, fit80, fit100


fits = plot_u3()


def e_me(k, r):

    MI_0 = 4e-7 * sp.pi
    N = 154
    RO_0 = 0.2

    citatel = 125 * RO_0**2 * k
    jmenovatel = 32 * r**2 * MI_0**2 * N**2

    return citatel / jmenovatel


for f, r in zip(fits, [0.02, 0.03, 0.04, 0.05]):

    k = f.params[0]
    err_k = f.errors[0]

    e_me_kr = e_me(k, r)
    err_e_me_kr = up_function(e_me, (k, r), (err_k, 0.0005))

    print(f"pro r = {r} e/m_e = {uf(e_me_kr, err_e_me_kr)}")
