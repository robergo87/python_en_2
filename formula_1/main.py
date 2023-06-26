class Driver:
    def __init__(self, turns, straights, pitstops, tires):
        self.turns = turns
        self.straights = straights
        self.pitstops = pitstops
        self.tires = tires

    def score(self, racetrack, laps):
        score = 0
        score += racetrack["turns"] * self.turns
        score += racetrack["straights"] * self.straights
        score += racetrack["pitstops"] * self.pitstops
        score = score * self.tires / (laps + self.tires - 20)
        return score


class DriverFerrari:
    def __init__(self, turns, straights, pitstops, tires):
        self.turns = turns
        self.straights = straights
        self.pitstops = pitstops
        self.tires = tires

    def score(self, racetrack, laps):
        score = 0
        score += racetrack["turns"] * self.turns
        score += racetrack["straights"] * self.straights
        score += racetrack["pitstops"] * self.pitstops
        score = score * self.tires / (laps + self.tires - 30)
        return score

drivers = {
    "Lewis Hamilton": Driver(8, 7, 9, 8),
    "George Russel": Driver(6, 7, 8, 6),
    "Max Verstappen": Driver(7, 10, 9, 9),
    "Sergio Perez": Driver(5,  10, 7, 10),
    "Charles Leclerc": DriverFerrari( 8, 9, 6, 7),
    "Carlos Saintz": DriverFerrari( 5, 6, 5, 5),
}
racetracks = {
    "monaco": {"turns": 0.7, "straights": 0.2, "pitstops": 0.1},
    "yokohama": {"turns": 0.4, "straights": 0.3, "pitstops": 0.3},
    "silverstone": {"turns": 0.3, "straights": 0.6, "pitstops": 0.1},
    "miami": {"turns": 0.2, "straights": 0.4, "pitstops": 0.4},
}

racetrack_name = input("Racetrack:")
laps = int(input("Number of Laps"))


positions = {}
start_score = 0
while True:
    name = input("Driver Name:")
    if not name:
        break;
    positions[name] = start_score
    start_score -= 4

for lap in range(laps):
    for name, score in positions.items():
        driver = drivers[name]
        positions[name] = score + driver.score(racetracks[racetrack_name], laps)
print()
for name, score in positions.items():
    print(f"driver: {name} score: {score}")
