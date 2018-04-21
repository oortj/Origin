# Write your median_bins and median_approx functions here.
import numpy as np

def median_bins(numbers, b):

    numberarray = np.array(numbers, dtype='float')
    mn = np.mean(numberarray, axis = 0)
    sd = np.std(numberarray, axis = 0)
    
    # the number of elements smaller than mn - sd:
    minval = mn - sd
    maxval = mn + sd
    
    binarray = numberarray[np.where(numberarray < minval)]
    smallnum = len(binarray)
    
    hst = np.histogram(numberarray, bins=b, range=(minval, maxval))
    
    return(mn, sd, smallnum, np.asarray(hst[0], dtype='float'))


def median_approx(numbers, bins):
    md = 0

    res = median_bins(numbers, bins)
    mn = res[0]
    sd = res[1]
    smallnum = res[2]
    hst = res[3]

    total = smallnum
    countmax = (len(numbers) + 1) / 2
    i = 0

    # find the bin where the sum of the values does not exceed (N + 1 ) /2
    while not (total >= countmax):
        total += hst[i]
        i += 1
        
    bin_width = (2*sd)/bins
    md = mn - sd + bin_width * (i -1 + 0.5)

    return(md)


# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Run your functions with the first example in the question.
    print(median_bins([1, 1, 3, 2, 2, 6], 3))
    print(median_approx([1, 1, 3, 2, 2, 6], 3))

    # Run your functions with the second example in the question.
    print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
    print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
