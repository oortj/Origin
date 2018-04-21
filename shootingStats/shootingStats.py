#!pythonw
import csv
from datetime import date
from session import ShootingSession
from operator import attrgetter
import matplotlib.pyplot as plt
 
sessionList = [] 
 
with open('TargetScanData.csv', newline='', encoding="utf-8") as File:  
	reader = csv.reader(File)
	next(reader, None)
	for row in reader:
		session = ShootingSession(row[0],row[1],row[2],row[3],row[4],row[5], row[6], row[7], row[8], row[9])
		sessionList.append(session)
		

lastYear = [s for s in sessionList if s.datum.year == date.today().year -1]
thisYear = [s for s in sessionList if s.datum.year == date.today().year]
thisYear.sort(key = attrgetter('score'), reverse = True)
lastYear.sort(key = attrgetter('score'), reverse = True)

average = round((lastYear[0].score + lastYear[1].score + lastYear[2].score)/3)
print("Gemiddelde van de 3 hoogste scores in {}: {}".format(date.today().year -1, average))
print("({}, {}, {})".format(lastYear[0].score, lastYear[1].score, lastYear[2].score))

average = round((thisYear[0].score + thisYear[1].score + thisYear[2].score)/3)
print("Gemiddelde van de 3 hoogste scores in {}: {}".format(date.today().year, average))
print("({}, {}, {})".format(thisYear[0].score, thisYear[1].score, thisYear[2].score))

sessionList.sort(key=attrgetter('datum'), reverse=False)

x = [x.datum for x in sessionList]
y = [x.score for x in sessionList]

# for i, d in enumerate(x):
# 	print('{} - {} - {}'.format(d, y[i], r[i]))

plt.plot(x, y, label="scores")
plt.scatter(x, y)
plt.legend()

plt.show()