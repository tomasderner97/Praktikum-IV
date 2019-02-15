from custom_utils.science.imports import *
from custom_utils.science import basics as sb
from matplotlib import ticker


def calibration_curve(channel):

    A = -4.955430E-002
    B = 4.477776E-001
    C = 2.606223E-008

    return C * channel**2 + B * channel + A


def plot_calibration(show=False, save=False):

    x = sp.arange(8000)

    with sb.latex_style():

        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.plot(x, calibration_curve(x))

        ax.set_xlabel(r"Kanál")
        ax.set_ylabel(r"E [keV]")
        ax.legend()
        fig.tight_layout()

        if show:
            plt.show()
        if save:
            fig.savefig("../fig/calibration.pdf")

        plt.close(fig)


df_kalib = sb.dataframe_from_csv("../data/kalibrace_ra226.Spe", header=None)
df_cesium = sb.dataframe_from_csv("../data/cs137.Spe", header=None)
df_sul = sb.dataframe_from_csv("../data/sul.Spe", header=None)

df = pd.DataFrame()
df["E"] = calibration_curve(df_kalib.index.values)
df["ra"] = df_kalib[0]
df["cs"] = df_cesium[0]
df["na"] = df_sul[0]


def plot_spectra(show=False, save=False):

    with sb.latex_style():

        fig, axs = plt.subplots(nrows=3, figsize=(11, 8.5))

        axs[0].plot(df.E, df.ra, "k", lw=0.5, label="Ra")
        axs[1].plot(df.E, df.cs, "k", lw=0.5, label="Cs")
        axs[2].plot(df.E, df.na, "k", lw=0.5, label="Na")

        axs[0].set_xlim(0, 2500)
        axs[0].xaxis.set_major_locator(ticker.MultipleLocator(200))
        axs[0].xaxis.set_minor_locator(ticker.MultipleLocator(50))

        axs[0].text(351.92 + 10, 3500, "$\\num{351.92}$")
        axs[0].text(609.34 + 10, 2000, "$\\num{609.34}$")
        axs[0].text(1120.29, 1000, "$\\num{1120.29}$", horizontalalignment="center")
        axs[0].text(1764.50, 600, "$\\num{1764.50}$", horizontalalignment="center")
        axs[0].text(2204.10, 140, "$\\num{2204.10}$", horizontalalignment="center")

        axs[1].set_xlim(0, 2300)
        axs[1].xaxis.set_major_locator(ticker.MultipleLocator(200))
        axs[1].xaxis.set_minor_locator(ticker.MultipleLocator(50))

        axs[1].text(668, 2000, "FEP")
        axs[1].text(478, 370, "CH", horizontalalignment="center")
        axs[1].text(563, 130, "DCR", horizontalalignment="center")
        axs[1].text(186, 630, "ZR", horizontalalignment="center")
        axs[1].text(609, 230, "Ra", horizontalalignment="center")
        axs[1].text(1120, 100, "Ra", horizontalalignment="center")
        axs[1].text(1765, 90, "Ra", horizontalalignment="center")
        axs[1].text(2204, 30, "Ra", horizontalalignment="center")
        axs[1].text(1461, 110, "K", horizontalalignment="center")

        axs[2].set_xlim(0, 3000)
        axs[2].xaxis.set_major_locator(ticker.MultipleLocator(200))
        axs[2].xaxis.set_minor_locator(ticker.MultipleLocator(50))

        axs[2].text(2754 + 10, 465, "FEP1")
        axs[2].text(1369 + 10, 1470, "FEP2")
        axs[2].text(1732, 440, "DEP1", horizontalalignment="center")
        axs[2].text(2243, 215, "SEP1", horizontalalignment="center")
        axs[2].text(511, 250, "ANI", horizontalalignment="center")
        axs[2].text(2520, 60, "CH1", horizontalalignment="center")
        axs[2].text(1150 + 20, 167, "CH2", horizontalalignment="center")
        axs[2].text(240, 532, "ZR", horizontalalignment="center")

        for ax in axs:
            ax.set_ylabel(r"Počet událostí")
            ax.set_yscale("log")
            ax.set_xlabel(r"E [keV]")
            ax.legend()

        fig.tight_layout()

        if show:
            plt.show()
        if save:
            fig.savefig("../fig/spectra2.pdf")

        plt.close(fig)


cs_peaks = {
    "FEP": {
        "mean": 661.66,
        "fwhm": 1.87,
        "n": 35184,
        "e_n": 200,
        "desc": "Absorpční pík"
    },
    "Ra1": {
        "mean": 609.37,
        "fwhm": 1.62,
        "n": 407,
        "e_n": 80,
        "desc": "Pozadí, \\textsuperscript{226}Ra"
    },
    "Ra2": {
        "mean": 1120.19,
        "fwhm": 2.37,
        "n": 354,
        "e_n": 45,
        "desc": "Pozadí, \\textsuperscript{226}Ra"
    },
    "Ra3": {
        "mean": 1764.55,
        "fwhm": 2.26,
        "n": 338,
        "e_n": 26,
        "desc": "Pozadí, \\textsuperscript{226}Ra"
    },
    "Ra4": {
        "mean": 2204.35,
        "fwhm": 2.66,
        "n": 114,
        "e_n": 15,
        "desc": "Pozadí, \\textsuperscript{226}Ra"
    },
    "K": {
        "mean": 1460.78,
        "fwhm": 1.95,
        "n": 386,
        "e_n": 23,
        "desc": "Pozadí, \\textsuperscript{40}K"
    }
}

na_peaks = {
    "FEP1": {
        "mean": 2754.36,
        "fwhm": 2.59,
        "n": 5220,
        "e_n": 74,
        "desc": "Absorpční pík"
    },
    "DEP1": {
        "mean": 1732.12,
        "fwhm": 2.22,
        "n": 1914,
        "e_n": 52,
        "desc": "Dvou-únikový pík"
    },
    "SEP1": {
        "mean": 2243.13,
        "fwhm": 2.44,
        "n": 1019,
        "e_n": 45,
        "desc": "Jedno-únikový pík"
    },
    "FEP2": {
        "mean": 1368.70,
        "fwhm": 2.02,
        "n": 11435,
        "e_n": 114,
        "desc": "Absorpční pík"
    },
    "ANI": {
        "mean": 511,
        "fwhm": 2.02,
        "n": 332,
        "e_n": 46,
        "desc": "Anihilační pík"
    },
}

cs_peaks = pd.DataFrame.from_dict(cs_peaks, orient="index")
na_peaks = pd.DataFrame.from_dict(na_peaks, orient="index")


def fwhm_to_sigma(fwhm):

    const = 2 * sp.sqrt(2 * sp.log(2))
    return fwhm / const


cs_peaks["sigma"] = fwhm_to_sigma(cs_peaks["fwhm"])
na_peaks["sigma"] = fwhm_to_sigma(na_peaks["fwhm"])


cs_col_props = [
    "mean $E$ [keV] 4.2",
    "fwhm FWHM [keV] 1.2",
    "sigma $\\sigma_E$ [keV] 1.2",
    "n $N$ [] 5.0",
    "e_n $\\sigma_N$ [] 3.0",
    "desc Popis",
    ["index", "V grafu"]
]

na_col_props = [
    "mean $E$ [keV] 4.2",
    "fwhm FWHM [keV] 1.2",
    "sigma $\\sigma_E$ [keV] 1.2",
    "n $N$ [] 5.0",
    "e_n $\\sigma_N$ [] 3.0",
    "desc Popis",
    ["index", "V grafu"]
]
