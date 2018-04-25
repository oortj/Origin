#!pythonw
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

data = pd.ExcelFile("obes-phys-acti-diet-eng-2017-tab.xlsx")
#df = pd.read_csv("time_series_data_1516.csv", encoding='utf-8')

# Read 2nd section, by age
data_age = data.parse(u'Table 2', skiprows=7, skipfooter=14)

# Drop empties
data_age.dropna(axis=1, how='all', inplace=True)
data_age.dropna(axis=0, how='all', inplace=True)

# Rename
data_age.rename(columns={u'Year4,5': u'Year'}, inplace=True)
data_age.rename(columns={u'All persons6': u'All persons'}, inplace=True)

# data_age['Year'].replace("/", "-", regex=True, inplace=True)
data_age['Year'] = data_age['Year'].str.slice(0,4).astype(str)
data_age.Year = pd.to_datetime(data_age['Year'], format='%Y')

data_age.set_index(['Year'], drop=True, inplace=True)

# Drop the total column and plot
data_age_minus_total = data_age.drop('All persons', axis=1)

print(data_age_minus_total)

print(data_age_minus_total.columns.values.tolist())

print(data_age_minus_total.index)
print(data_age_minus_total.index.dtype)
print(type(data_age_minus_total.index))

# # Plot
fig, ax = plt.subplots(figsize=(15,7))
data_age_minus_total.plot(ax=ax)

#set ticks every week
#ax.xaxis.set_major_locator(mdates.YearLocator())
#set major ticks format
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
 
plt.show()

plt.close()
fig, ax = plt.subplots(figsize=(15,7))
# # Plot children vs adults
data_age_minus_total['Under 16'].plot(label="Under 16", ax=ax)
data_age_minus_total['35 to 44'].plot(label="35-44", ax=ax)
plt.legend(loc="upper left")
plt.show()


