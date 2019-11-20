from scireputils.dataframes import dataframe_from_csv

from project_wide import calibration


def get_doublets():
    df = dataframe_from_csv("../data/doublets.csv")
    df["lambdas"] = calibration(df["degrees"])
    df["lambdas"] = round(df["lambdas"], 1)
    df["table_values"] = round(df["table_values"], 1)

    df["deltas_table"] = df["table_values"] - df["table_values"].shift(-1)
    df["deltas_measured"] = df["lambdas"] - df["lambdas"].shift(-1)
    return df


