from statistics import mean

def calculate_mean(fluxes):
    m = sum(fluxes)/len(fluxes)
    return m

    #fluxes = [23.3, 42.1, 2.0, -3.2, 55.6]
    #m = mean(fluxes)
    #print(m)

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Run your `calculate_mean` function with examples:
    mean = calculate_mean([1,2.2,0.3,3.4,7.9])
    print(mean)