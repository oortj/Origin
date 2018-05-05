import numpy as np


def mean_datasets(files):
    data = []

    for file in files:
        data.append(np.loadtxt(file, delimiter=','))

    mean = np.mean(data, axis=0)
    res = np.round(mean, decimals=1)

    return(res)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Run your `calculate_mean` function with examples:
    print(mean_datasets(['../csv/data1.csv', '../csv/data2.csv', '../csv/data3.csv']))
