# Write your mean_fits function here:
from astropy.io import fits
import numpy as np


def mean_fits(images):
    data = []

    for img in images:
        hdulist = fits.open(img)
        data.append(hdulist[0].data)

    mean = np.mean(data, axis=0)

    return(mean)


if __name__ == '__main__':

  # Test your function with examples from the question
  data = mean_fits(['fits_images/image0.fits', 'fits_images/image1.fits',
                    'fits_images/image2.fits', 'fits_images/image3.fits', 'fits_images/image4.fits'])
  print(data[100, 100])

  # You can also plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()
