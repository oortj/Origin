from statistics import mean

def calculate_mean(fluxes):
    m = sum(fluxes)/len(fluxes)
    return m

if __name__ == '__main__':
    fluxes = [1,2.2,0.3,3.4,7.9]
    # mean = calculate_mean(fluxes)
    print(mean(fluxes))
