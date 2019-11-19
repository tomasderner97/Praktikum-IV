from custom_utils.science.imports import *
from custom_utils.science import basics as sb

sb.use_mpl_latex_style()

df = sb.dataframe_from_csv("../data/u4.csv")
print(df)

cp = [
    ["count", "Počet událostí", "", "4.0"],
    ["sigma", r"Chyba střední hodnoty $\sigma$", "", "1.3"],
    ["err", "Chyba chyby", "", "1.3"]
]

# print(sb.df_to_booktabs_table(df, cp))


def plot_u5(show=False, save=False):

    fig = plt.figure(figsize=[6, 3])
    ax = fig.add_subplot(111)

    ax.errorbar(df["count"], df["sigma"], yerr=df["err"], fmt="kx", capsize=3, elinewidth=0.5)

    ax.set_xlabel(r"Počet událostí")
    ax.set_ylabel(r"Chyba střední hodnoty $\sigma$")
    # ax.legend()
    fig.tight_layout()

    if show:
        plt.show()
    if save:
        fig.savefig("../fig/u5.pdf")

    plt.close(fig)


# plot_u5(False, True)
