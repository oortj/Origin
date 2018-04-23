#!pythonw
import pandas as pd
from datetime import date

df = pd.read_csv('TargetScanData.csv', index_col=0, parse_dates=['Event Date'])

df['Score'] = df['Score'].str.slice(0,3).astype(int)

datum = date(int('2018'),int('01'),int('01'))
currentYear = df[(df['Event Date'] > datum)]

print(df.describe().transpose())
print(currentYear.describe().transpose())

