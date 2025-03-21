class PirateRecord:
    def __init__(self):
        # added fatigue property
        self.Row = 0
        self.Column = 0
        self.Score = 100
        self.DigTime = 0.0
        self.TreasureFound = False
        self.NumberOfCoinsFound = 0
        self.Fatigue = 0

def ResetPirateRecord(Pirate):
    # added fatigue property
    Pirate.Row = 0
    Pirate.Column = 0
    Pirate.Score = 100
    Pirate.DigTime = 0.0
    Pirate.TreasureFound = False
    Pirate.NumberOfCoinsFound = 0
    Pirate.Fatigue = 0

def PirateDigs(Map, HiddenMap, Pirate):
    if HiddenMap[Pirate.Row][Pirate.Column] != SAND:
        DisplayFind(Map, Pirate, HiddenMap[Pirate.Row][Pirate.Column])
    else:
        print("Nothing found")
    # made decrease in score a function of fatigue
    multiplier = 0
    if Pirate.Fatigue >= 3:
        multiplier = Pirate.Fatigue - 2
    Pirate.Score -= (10 + multiplier*2)
    Pirate.DigTime += 1.75
    # increase fatigue with every dig
    Pirate.Fatigue += 1
    print("Score:", Pirate.Score)