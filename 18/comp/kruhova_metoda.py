from custom_utils.science.imports import *
from custom_utils.science import basics as sb
from matplotlib.ticker import MultipleLocator
from PIL import Image

PIXEL_SIDE = 5.28125e-007 * 1e6

img1 = Image.open("../data/Fig_005.tif")  # 65
img2 = Image.open("../data/Fig_006.tif")  # 51
img3 = Image.open("../data/Fig_007.tif")  # 59
img4 = Image.open("../data/Fig_008.tif")  # 53

arr1 = sp.asarray(img1)
arr2 = sp.asarray(img2)
arr3 = sp.asarray(img3)
arr4 = sp.asarray(img4)

H, W = arr1.shape
with sb.latex_style():

    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(7.5, 6.9), sharex=True, sharey=True)

    axs[0, 0].imshow(arr1, cmap="gray", interpolation="spline36",
                     extent=(0, W * PIXEL_SIDE, H * PIXEL_SIDE, 0))
    axs[0, 1].imshow(arr2, cmap="gray", interpolation="spline36",
                     extent=(0, W * PIXEL_SIDE, H * PIXEL_SIDE, 0))
    axs[1, 0].imshow(arr3, cmap="gray", interpolation="spline36",
                     extent=(0, W * PIXEL_SIDE, H * PIXEL_SIDE, 0))
    axs[1, 1].imshow(arr4, cmap="gray", interpolation="spline36",
                     extent=(0, W * PIXEL_SIDE, H * PIXEL_SIDE, 0))
    axs[0, 0].set_ylabel("$\si{\micro\metre}$")
    axs[1, 0].set_ylabel("$\si{\micro\metre}$")
    axs[1, 0].set_xlabel("$\si{\micro\metre}$")
    axs[1, 1].set_xlabel("$\si{\micro\metre}$")

    for ax in axs.flatten():
        ax.xaxis.set_major_locator(MultipleLocator(100))

        circle = plt.Circle((265, 240), 210, linewidth=1, fill=False, color="white")
        ax.add_patch(circle)

    fig.tight_layout()
    # fig.savefig("../fig/kruh.pdf")
    # plt.show()

n = uf(57, 5.9)
D = 210 * 2
d = 3 * sp.pi / 2 * D / n
