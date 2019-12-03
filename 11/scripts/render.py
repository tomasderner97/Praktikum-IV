import subprocess

from scireputils.latex_templates import render_template, make_figure_float, make_table_float, \
    dataframe_to_booktabs_table

from scripts.heating import get_heating
from spread import get_spread

TEMPLATE_FILE = "../templates/main.tex"
LATEX_FILE = "../latex/main.tex"

LATEX_COMMAND = [
    "pdflatex",
    "-file-line-error",
    "-interaction=nonstopmode",
    "-synctex=1",
    "-output-format=pdf",
    "-output-directory=../output",
    "-aux-directory=../auxiliary",
    "-include-directory=../classfiles",
    "-include-directory=../latex",
    LATEX_FILE
]

OPEN_PDF_COMMAND = [
    "sumatrapdf",
    "../output/main.pdf"
]

heating_df = get_heating()
heating_table_code = dataframe_to_booktabs_table({"T1": heating_df[:6]["T"],
                                                  "U1": heating_df[:6]["U"],
                                                  "T2": heating_df[6:]["T"],
                                                  "U2": heating_df[6:]["U"]
                                                  },
                                                 [("T1", "t", "$[\\si{\\celsius}]$", "3.0"),
                                                  ("U1", "U", "[V]", "1.2"),
                                                  ("T2", "t", "$[\\si{\\celsius}]$", "3.0"),
                                                  ("U2", "U", "[V]", "1.2"),
                                                  ])

spread_table_code = dataframe_to_booktabs_table(get_spread()[1:],
                                                [("I", "$I$", "[A]", "1.2"),
                                                 ("B", "$B$", "[T]", "1.2"),
                                                 ("dx", "$\\Delta x$", "[mm]", "1.2"),
                                                 ("q", "$q$", "[mm]", "1.2"),
                                                 (
                                                     "grad_B",
                                                     "$\\frac{\\partial B}{\\partial x}$",
                                                     "$[\\si{\\tesla\\per\\milli\\metre}]$",
                                                     "1.3")])

tab_heating = make_table_float(heating_table_code, "heating", "Hodnoty závislosti odezvy detektoru na tepotě v pícce")
tab_spread = make_table_float(spread_table_code, "spread", "Naměřené hodnoty vzdálenosti maxim píků závislostí na poli "
                                                           "v analyzátoru")
fig_heating = make_figure_float("heating.pdf", "heating", "Závislost odezvy detektoru na teplotě v pícce",
                                position="h!")
fig_0A_fit = make_figure_float("0A_fit.pdf", "0A_fit", "Závislost odezvy detektoru na jeho poloze pro nulové pole "
                                                       "v analyzátoru", position="h!")
fig_curves = make_figure_float("curves.pdf", "curves", "Závislosti odezvy detektoru na jeho poloze pro různá pole "
                                                       "v analyzátoru", position="h!")
fig_spread = make_figure_float("spread.pdf", "spread", "Lineární fit pro výpočet Bohrova magnetonu",
                               position="h!")

render_template(TEMPLATE_FILE,
                LATEX_FILE,
                tab_heating=tab_heating,
                fig_heating=fig_heating,
                tab_spread=tab_spread,
                fig_0A_fit=fig_0A_fit,
                fig_curves=fig_curves,
                fig_spread=fig_spread,
                )

subprocess.run(LATEX_COMMAND, check=True)
subprocess.run(OPEN_PDF_COMMAND, check=True)
