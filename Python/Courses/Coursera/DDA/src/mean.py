def calculate_mean(fluxes):
    m = sum(fluxes)/len(fluxes)
    return m

if __name__ == '__main__':
    mean = calculate_mean([1,2.2,0.3,3.4,7.9])
    print(mean)
