import numpy as np

def calc_stats(file):
    data= []

    for line in open(file):
        data.append(line.strip().split(','))
    
    return(data)


if __name__ == '__main__':
    d = calc_stats('../csv/data.csv')
    print(d)