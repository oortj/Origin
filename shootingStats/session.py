from datetime import datetime, date


class ShootingSession:

    def __init__(self, sessionId, datum, shots, score, percentage, windage, elevation, meanRadius, maxSpread, notes):
        self.sessionId = sessionId
        self.datum = datetime.strptime(datum, '%d/%m/%Y').date()
        self.shots = int(shots)
        self.score = int(score[0:3])
        self.percentage = float(percentage.replace(",","."))
        self.windage = float(windage)
        self.elevation = float(elevation)
        self.meanRadius = float(meanRadius)
        self.maxSpread = float(maxSpread)
        self.notes = notes

    def function(self):
        print(self.sessionId)