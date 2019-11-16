from custom_utils.science.basics import dataframe_from_csv

from project_wide import calibration


def get_doublets():
    df = dataframe_from_csv("../data/doublets.csv")
    df["lambdas"] = calibration(df["degrees"])
    df["lambdas"] = round(df["lambdas"], 1)
    df["table_values"] = round(df["table_values"], 1)
    return df


