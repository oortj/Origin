#!pythonw
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

df = pd.read_csv("Leefstijl__persoonskenmerken_27042018_174215.csv", skiprows=0, delimiter=";", decimal=",", encoding = "ISO-8859-1")

df.dropna(axis=1, how='all', inplace=True)
df.dropna(axis=0, how='all', inplace=True)

df.rename(columns={u'Kenmerken personen': u'Kenmerken'}, inplace=True)

df.set_index([u'Kenmerken'], drop=True, inplace=True)

df_leeftijd = df.loc[df.index.str.contains('Onderwijs') | df.index.str.contains('Totaal')]

df_leeftijd['Rookgedrag, 12 jaar of ouder/Rookstatus/Rokers (%)'].replace('', np.nan, inplace=True)
df_leeftijd.dropna(subset=['Rookgedrag, 12 jaar of ouder/Rookstatus/Rokers (%)'], inplace=True)

print(df_leeftijd['Rookgedrag, 12 jaar of ouder/Rookstatus/Rokers (%)'])

fig, ax = plt.subplots(figsize=(12,7))
plt.xticks(rotation=45)
plt.bar(x=df_leeftijd.index, height=df_leeftijd['Rookgedrag, 12 jaar of ouder/Rookstatus/Rokers (%)'])
plt.legend(loc="upper left")
plt.show()

# print(df_leeftijd)

