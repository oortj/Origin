import numpy as np

def calc_stats(file):
    data = np.loadtxt(file, delimiter=',')
    return(np.round(np.mean(data),decimals=1), np.round(np.median(data), decimals=1))

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Run your `calculate_mean` function with examples:
    print(calc_stats('csv/data.csv'))