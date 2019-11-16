import matplotlib.pyplot as plt
import numpy as np
from custom_utils.science.basics import latex_style
from customutils2.science.basics import dataframe_from_csv

from project_wide import calibration


def get_calibration_points():
    return dataframe_from_csv("../data/calibration.csv")


def plot_calibration(name=""):
    with latex_style():
        fig, ax = plt.subplots()

        degrees = np.linspace(900, 3350, 1000)
        lambdas = calibration(degrees)
        calibration_pts = get_calibration_points()

        ax.plot(degrees, lambdas, ":", c="grey", label=r"Kalibrační křivka")
        ax.plot(calibration_pts["degrees"], calibration_pts["lambda"], "kx", label=r"Naměřené body")

        ax.set_xlabel("Obecné jednotky")
        ax.set_ylabel(r"$\lambda\si{nm}$")
        ax.autoscale(axis="x", tight=True)
        ax.legend()

        fig.tight_layout()

        fig.savefig(f"../plot/{name or 'plot'}.pdf")

    return fig, ax


if __name__ == '__main__':
    plot_calibration()
    plt.show()
