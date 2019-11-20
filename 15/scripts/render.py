from scireputils.latex_templates import render_template

plot_calibration = r"""
\begin{figure}[h]
    \centering
    \includegraphics{plots.pdf}
    \caption{}
    \label{fig:fig}
\end{figure}
"""

render_template("../templates/main.tex",
                "../latex/main.tex",
                plot_calibration=plot_calibration)
