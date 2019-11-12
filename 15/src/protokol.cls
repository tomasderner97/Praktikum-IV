\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{protokol}[2017/09/20]

\LoadClass[11pt]{article}
\RequirePackage[utf8]{inputenc}
\RequirePackage[czech]{babel}

\RequirePackage[margin=3cm]{geometry}
\RequirePackage{fancyhdr}
\RequirePackage[decimalsymbol=comma]{siunitx}
\RequirePackage{float}
%\RequirePackage{subfiles}
\RequirePackage{graphicx}
%\RequirePackage{pgfplotstable}
\RequirePackage{booktabs}
\RequirePackage{verbatim}
\RequirePackage{amsmath}
\RequirePackage[hidelinks=true]{hyperref}
\RequirePackage{icomma}
\RequirePackage{siunitx}
%\RequirePackage[]{xcolor}
\RequirePackage{wrapfig}
\RequirePackage{caption}
\RequirePackage{lipsum}

\captionsetup[figure]{skip=0pt}

\RequirePackage{etoolbox}
\preto\tabular{\shorthandoff{-}}

\setlength{\headheight}{14pt}

\begin{comment}
%% hack to make cmidrule work
\makeatletter
\begingroup
\toks0=\expandafter{\@cline{#1}-{#2}\@nil}
\@ifpackageloaded{booktabs}{%
  \toks2=\expandafter{\@@@cmidrule[{#1}-{#2}]{#3}{#4}}%
}{}
\catcode`-=\active
\edef\x{\gdef\unexpanded{\@cline#1-#2\@nil}{\the\toks0}}\x
\@ifpackageloaded{booktabs}{%
  \edef\x{\gdef\unexpanded{\@@@cmidrule[#1-#2]#3#4}{\the\toks2}}\x
}{}
\endgroup
\makeatother
%% end of hack
\end{comment}

\pagestyle{fancy}
\fancyhead{}
\parindent 2ex
%\setlength{\parskip}{\baselineskip}
\graphicspath{{plot/}{./}{fig/}{../plot/}{../fig/}}

\newcommand{\leftheader}[1]{\fancyhead[L]{#1}}
\newcommand{\centerheader}[1]{\fancyhead[C]{#1}}
\newcommand{\rightheader}[1]{\fancyhead[R]{#1}}

\newcommand{\cz}[1]{\textit{#1}}

\sisetup{separate-uncertainty=true}