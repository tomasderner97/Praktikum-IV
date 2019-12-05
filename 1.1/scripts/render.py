import os

from scireputils.latex_templates import render_template, compile_latex_to_pdf, make_table_float, make_figure_float

from project_wide import TEMPLATES_PATH, LATEX_PATH, OUTPUT_PATH

# dataframe_to_booktabs_table(get_errors(), (("N", "$N$"), ("err", "$s_{\\mu}$")), "../tables/errors.tex")

template_params = {
    "tab_errors": make_table_float("../tables/errors.tex",
                                   "errors",
                                   "Závislost hodnoty chyby pozice píku Z bozonu na počtu měření",
                                   external_table=True),
    "tab_particles": make_table_float("../tables/particles.tex",
                                      "particles",
                                      "Částice, kterých se týká toto praktikum",
                                      external_table=True),
    "fig_fit_errors": make_figure_float("fit_errors.pdf",
                                        "fit_errors",
                                        "Závislost hodnoty chyby pozice píku Z bozonu na počtu měření",
                                        position="h!")
}

TEMPLATE_PATH = os.path.join(TEMPLATES_PATH, "main.tex")
LATEX_OUT_PATH = os.path.join(LATEX_PATH, "main.tex")
PDF_PATH = os.path.join(OUTPUT_PATH, "main.pdf")

render_template(TEMPLATE_PATH,
                LATEX_OUT_PATH,
                **template_params
                )
compile_latex_to_pdf(LATEX_OUT_PATH,
                     PDF_PATH)
