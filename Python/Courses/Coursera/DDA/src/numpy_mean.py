import numpy as np

def calc_stats(file):
    data = np.loadtxt(file, delimiter=',')
    m = (np.round(np.mean(data),1), np.round(np.median(data),1))
    return(m)

if __name__ == '__main__':
    mean = calc_stats('../csv/data.csv')
    print(mean)

