import subprocess

from scireputils.latex_templates import render_template, make_figure_float, make_table_float, \
    dataframe_to_booktabs_table

from scripts.heating import get_heating

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

table_code = dataframe_to_booktabs_table(get_heating(),
                                         [("T", "t", "$[\\si{\\celsius}]$", "3.0"),
                                          ("U", "U", "[V]", "1.2")])

tab_heating = make_table_float(table_code, "heating", "Hodnoty závislosti odezvy detektoru na tepotě v pícce")
fig_heating = make_figure_float("heating.pdf", "heating", "Závislost odezvy detektoru na teplotě v pícce", position="h!")

render_template(TEMPLATE_FILE,
                LATEX_FILE,
                tab_heating=tab_heating,
                fig_heating=fig_heating,
                )

subprocess.run(LATEX_COMMAND, check=True)
subprocess.run(OPEN_PDF_COMMAND, check=True)
