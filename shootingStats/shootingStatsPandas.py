#!pythonw
import pandas as pd
from datetime import date, datetime

df = pd.read_csv('TargetScanData.csv', index_col=0, parse_dates=['Event Date'])
datum = date(int('2018'),int('01'),int('01'))
currentYear = df[(df['Event Date'] > datum) & (df['Mean Radius'] < 20)]

print(currentYear)