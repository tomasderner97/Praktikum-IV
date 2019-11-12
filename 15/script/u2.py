import numpy as np
import matplotlib.pyplot as plt
import customutils2

plt.style.use(r"C:\Users\tomas\AppData\Roaming\Python\Python37\site-packages\customutils2\science\latex_style.mplstyle")

voltage = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    12,
    14,
    16,
    18,
    20,
    25,
    30,
    35,
    40,
    50,
    70,
    100,
    150,
    200,
    250,
    300,
    400,
    500
]
current_d6 = [
    0.1,
    0.3,
    1.1,
    2,
    2.8,
    3.6,
    4.3,
    5,
    5.6,
    6.2,
    6.7,
    7.3,
    7.9,
    8.4,
    8.7,
    8.9,
    9.3,
    9.7,
    10,
    10.3,
    10.4,
    10.9,
    11.3,
    11.5,
    12,
    12.3,
    12.4,
    12.5,
    12.7
]
current_d2 = [
    1.3,
    1.9,
    3.5,
    4.5,
    4.8,
    5,
    5.1,
    5.4,
    5.5,
    5.5,
    5.4,
    5.5,
    5.7,
    5.8,
    6,
    6.1,
    6.1,
    6.1,
    6,
    6.1,
    6.2,
    6.2,
    6.1,
    6.3,
    6.5,
    6.4,
    6.5,
    6.6,
    6.6,
]

fig, ax = plt.subplots()

ax.plot(voltage, current_d6, "x", label="$d = \SI{6}{cm}$")
ax.plot(voltage, current_d2, "+", ms=7, label="$d = \SI{2}{cm}$")

ax.set_xlabel(r"$U$[V]")
ax.set_ylabel(r"$I$[pA]")

ax.legend()

fig.tight_layout()
fig.savefig("../plot/u2.pdf")

