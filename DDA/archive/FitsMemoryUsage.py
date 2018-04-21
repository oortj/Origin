# Write your mean_fits function here:
from astropy.io import fits
import numpy as np
import time


def median_fits(images):
    start = time.perf_counter()
    data = []
    memtotal = 0

    for img in images:
        hdulist = fits.open(img)
        data.append(hdulist[0].data)
        memtotal += hdulist[0].data.nbytes

    mean = np.median(data, axis=0)
    end = time.perf_counter() - start

    return(mean, end, (memtotal / 1024))


if __name__ == '__main__':
    # Run your function with first example in the question.
    #result = median_fits(['fits_images/image0.fits', 'fits_images/image1.fits'])
    #print(result[0][100, 100], result[1], result[2])

    result = median_fits(
        ['fits_images/image{}.fits'.format(str(i)) for i in range(11)])
    print(result[0][100, 100], result[1], result[2])
