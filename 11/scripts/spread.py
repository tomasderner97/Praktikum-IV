import matplotlib.pyplot as plt
from scireputils.dataframes import dataframe_from_csv


def get_spread():
    return dataframe_from_csv("../data/spread.csv")



