#!pythonw
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('TargetScanData.csv', index_col=0, parse_dates=['Event Date'])

df['Score'] = df['Score'].str.slice(0,3).astype(int)
df['Notes'] = df['Notes'].str.strip()
df['Notes'] = df['Notes'].str.lower()
df['Notes'].replace("^(?!harr.*hamm.*)h.?mmerli( p?208.*)*", "Hammerli 208s", regex=True, inplace=True)
df['Notes'].replace("^.*sp20.*", "Hammerli SP20", regex=True, inplace=True)
df['Notes'].replace("^harr.*hamm.*", "Hammerli 208 Int", regex=True, inplace=True)
df['Notes'].replace("^.*(no20|no 20)", "Hammerli 208s", regex=True, inplace=True)
df['Notes'].replace('erekorps', '', regex=True, inplace=True)
df['Notes'].replace('zelfkennis / rangorde', '', regex=True, inplace=True)
df['Notes'].replace("^.*beretta.*", "Beretta 76", regex=True, inplace=True)
df['Notes'].replace("^.*colt.*22.*", "Colt 22", regex=True, inplace=True)
df['Notes'].replace("^.*fn.*browning.*", "FN Browning", regex=True, inplace=True)
df['Notes'].replace("^.*revolver.*", "Smith&Wesson 617", regex=True, inplace=True)
df['Notes'] = df['Notes'].fillna('Hammerli 208 Int')
df['Notes'] = df['Notes'].str.strip()

datum = date(int('2018'),int('01'),int('01'))
#currentYear = df[(df['Event Date'] > datum)]

df = df.sort_values(by=['Notes'],ascending=True)


''' Plotting '''

fig = plt.figure()

ax = fig.add_subplot(1,1,1)
ax.set_ylim(260,375)
major_ticks = np.arange(260, 375, 10)
minor_ticks = np.arange(260, 375, 5)

ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

# ax.grid(axis='y')

plt.grid(axis='y')

plt.xticks(rotation=45)
plt.bar(df.Notes, df.Score)
plt.show()

print(df.describe().transpose())
# print(currentYear.describe().transpose())

