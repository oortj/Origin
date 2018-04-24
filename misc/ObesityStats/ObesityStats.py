#!pythonw
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import numpy as np


data = pd.ExcelFile("obes-phys-acti-diet-eng-2017-tab.xlsx")

# Read 2nd section, by age
data_age = data.parse(u'Table 2', skiprows=7, skipfooter=14)

# Drop empties
data_age.dropna(axis=1, how='all', inplace=True)
data_age.dropna(axis=0, how='all', inplace=True)

# Rename unamed to year
data_age.rename(columns={u'Year4,5': u'Year'}, inplace=True)
data_age.rename(columns={u'All persons6': u'All persons'}, inplace=True)

data_age.set_index('Year', inplace=True)

# Drop the total column and plot
data_age_minus_total = data_age.drop('All persons', axis=1)

print(data_age_minus_total)

# # Plot

data_age_minus_total.plot()

plt.xticks(rotation=45)
plt.show()

# plt.close()

# # Plot children vs adults
# data_age['Under 16'].plot(label="Under 16")
# data_age['35 to 44'].plot(label="35-44")
# plt.legend(loc="upper right")
# plt.show()


