class PirateRecord:
    def __init__(self):
        # added property
        self.Row = 0
        self.Column = 0
        self.Score = 100
        self.DigTime = 0.0
        self.TreasureFound = False
        self.NumberOfCoinsFound = 0
        self.UsedDynamite = False

def ResetPirateRecord(Pirate):
    # added property
    Pirate.Row = 0
    Pirate.Column = 0
    Pirate.Score = 100
    Pirate.DigTime = 0.0
    Pirate.TreasureFound = False
    Pirate.NumberOfCoinsFound = 0
    Pirate.UsedDynamite = False

def CheckPath(Map, StartRow, StartColumn, EndRow, EndColumn, Direction):
    # made craters also not count as obstacles
    o = lambda x: x not in [SAND, CRATER]
    ObstacleFound = False
    if Direction == "N":
        for Row in range(EndRow, StartRow):
            if o(Map[Row][StartColumn]):
                ObstacleFound = True
    elif Direction == "NE":
        for i in range(1, StartRow - EndRow + 1):
            if o(Map[StartRow - i][StartColumn + i]):
                ObstacleFound = True
    elif Direction == "E":
        for Column in range(StartColumn + 1, EndColumn + 1):
            if o(Map[StartRow][Column]):
                ObstacleFound = True
    elif Direction == "SE":
        for i in range(1, EndRow - StartRow + 1):
            if o(Map[StartRow + i][StartColumn + i]):
                ObstacleFound = True
    elif Direction == "S":
        for Row in range(StartRow + 1, EndRow + 1):
            if o(Map[Row][StartColumn]):
                ObstacleFound = True
    elif Direction == "SW":
        for i in range(1, EndRow - StartRow + 1):
            if o(Map[StartRow + i][StartColumn - i]):
                ObstacleFound = True
    elif Direction == "W":
        for Column in range(EndColumn, StartColumn):
            if o(Map[StartRow][Column]):
                ObstacleFound = True
    elif Direction == "NW":
        for i in range(1, StartRow - EndRow + 1):
            if o(Map[StartRow - i][StartColumn - i]):
                ObstacleFound = True
    return ObstacleFound

def Boom(Map, HiddenMap, Pirate):
    # get indexes of surrounding squares
    Col = Pirate.Column
    Row = Pirate.Row
    Indexes = [[
        (Row+i, Col-1),
        (Row+i, Col),
        (Row+i, Col+1)
    ] for i in range(-1,2)]
    Indexes[1].pop(1)  # removes location of pirate

    print("BOOM!")
    for Row in Indexes:
        for Square in Row:
            FoundItem = HiddenMap[Square[0]][Square[1]]
            if FoundItem == TREASURE:
                # delete treasure
                HiddenMap[Square[0]][Square[1]] = SAND
                print("Oops...")
            elif FoundItem != SAND:
                # claims each item in the surrounding squares
                DisplayFind(Map, Pirate, FoundItem)
                Map[Pirate.Row][Pirate.Column] = SAND  # replace "discovered" items on pirate square
            if Map[Square[0]][Square[1]] != WATER:
                # replaces non-water squares with craters
                Map[Square[0]][Square[1]] = CRATER
    Pirate.UsedDynamite = True

def PirateUsesDynamite(Map, HiddenMap, Pirate):
    # checks for UsedDynamite flag
    if Pirate.UsedDynamite:
        print("You have already used your dynamite.")
        return
    Boom(Map, HiddenMap, Pirate)

def GetPirateAction(Map, MapSize, HiddenMap, Pirate, Answer):
    # added new dynamite (X) option
    Answer = input("Pirate to walk (W) or dig (D), or use dynamite (X), to finish game press Enter: ")
    while not (Answer == "W" or Answer == "D" or Answer == PRESSED_ENTER or Answer == "X"):
        Answer = input("Pirate to walk (W) or dig (D), or use dynamite (X), to finish game press Enter: ")
    if Answer == "W":
        PirateWalks(Map, MapSize, HiddenMap, Pirate)
    elif Answer == "D":
        PirateDigs(Map, HiddenMap, Pirate)
    elif Answer == "X":
        PirateUsesDynamite(Map, HiddenMap, Pirate)
    return Answer