#!pythonw
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt

df = pd.read_csv('TargetScanData.csv', index_col=0, parse_dates=['Event Date'])

df['Score'] = df['Score'].str.slice(0,3).astype(int)
# df['Notes'] = df['Notes'].replace('', np.nan)
df['Notes'] = df['Notes'].str.strip()
df['Notes'].replace("^(?!Harr.*Hamm.*)H.?mmerli P?208.*", "Hammerli 208s", regex=True, inplace=True)
df['Notes'].replace("^Harr.*Hamm.*", "Hammerli 208 Int", regex=True, inplace=True)
df['Notes'].replace("^.*(no20|no 20)", "Hammerli 208s", regex=True, inplace=True)
df['Notes'] = df['Notes'].fillna('Hammerli 208 Int')

# df['Notes'].replace("(!Harr.*)H.?mm.*208.*", "Hammerli 208s", regex=True, inplace=True)

datum = date(int('2018'),int('01'),int('01'))
currentYear = df[(df['Event Date'] > datum)]

plt.figure()
plt.barh(df['Notes'], df['Score'])
plt.xticks(rotation='vertical')
plt.show()

# print(df)
# print(df.describe().transpose())
# print(currentYear.describe().transpose())

