import numpy as np

def mean_datasets(files):
    res = []
    for file in files:
        data = np.loadtxt(file, delimiter=',')
        res.append(data)

    mean = np.mean(res, axis=0)
    rnd = np.round(mean, 1)
    return(rnd)


if __name__ == '__main__':
    print(mean_datasets(['../csv/data1.csv', '../csv/data2.csv', '../csv/data3.csv']))