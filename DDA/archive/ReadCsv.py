import numpy as np

data = []
for line in open('csv/data.csv'):
    data.append(line.strip().split(','))
    
data = np.asarray(data, float)    
    
print(data)