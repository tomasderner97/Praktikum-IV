import numpy as np
import matplotlib.pyplot as plt
import customutils2

plt.style.use(r"C:\Users\tomas\AppData\Roaming\Python\Python37\site-packages\customutils2\science\latex_style.mplstyle")

voltage = [
    0.9,
    0.97,
    1.01,
    1.04,
    1.06,
    1.13,
    1.17,
    1.2,
    1.25,
    1.27,
    1.3,
    1.32,
    1.34,
    1.37,
    1.39,
    1.42,
    1.45,
    1.5,
]
impuls = [
    1,
    2,
    3,
    4,
    5,
    10,
    15,
    20,
    30,
    40,
    60,
    80,
    100,
    150,
    200,
    300,
    400,
    600,
]

fig, ax = plt.subplots()

ax.plot(voltage, impuls, "x")
ax.set_yscale("log")

ax.set_xlabel(r"$U$[kV]")
ax.set_ylabel(r"$U_i$[mV]")

fig.tight_layout()
fig.savefig("../plot/u6.pdf")
