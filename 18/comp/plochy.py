from custom_utils.science.imports import *
from custom_utils.science import basics as sb

df = sb.dataframe_from_csv("../data/u3.csv")
df["v_olovo"] = df["olovo"] * 100 / (100 - df["necistota"])
df["v_cin"] = df["cin"] * 100 / (100 - df["necistota"])

# cp = [
#     "snimek Snímek n 1.0",
#     "cin cín [$\si{\percent}$] 2.1",
#     "olovo olovo [$\si{\percent}$] 2.1",
#     "necistota nečistota [$\si{\percent}$] 1.1",
#     ["v_cin", "cínu ve vzorku", "[$\si{\percent}$]", "2.1"],
#     ["v_olovo", "olova ve vzorku", "[$\si{\percent}$]", "2.1"],

# ]

# sb.df_to_booktabs_table(df, cp, "../tab/u3.tex")
