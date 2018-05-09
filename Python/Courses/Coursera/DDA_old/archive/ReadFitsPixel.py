import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt


def load_fits(img):
    hdulist = fits.open(img)

    data = hdulist[0].data

    return(np.unravel_index(data.argmax(), data.shape))


if __name__ == '__main__':
    # Run your `load_fits` function with examples:
    bright = load_fits('../fits_images/image2.fits')
    print(bright)

    hdulist = fits.open('../fits_images/image2.fits')
#    print(hdulist.info())
    data = hdulist[0].data
    plt.imshow(data, cmap=plt.cm.viridis)
    plt.xlabel('x-pixels (RA)')
    plt.ylabel('y-pixels (Dec)')
    plt.colorbar()
    plt.show()
