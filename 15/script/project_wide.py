from customutils2.science.basics import dataframe_from_csv

FIT_PARAMETERS = None


def fit_func(x, a, b, c, d, e, f):
    return ((((a * x + b) * x + c) * x + d) * x + e) * x + f


def get_fit_parameters():
    global FIT_PARAMETERS

    if not FIT_PARAMETERS:
        df = dataframe_from_csv("../data/calibration_params.csv")
        FIT_PARAMETERS = tuple(df["value"])

    return FIT_PARAMETERS


def calibration(degrees):
    return fit_func(degrees, *get_fit_parameters())