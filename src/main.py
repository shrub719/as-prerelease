# Skeleton Program for the AQA AS Summer 2025 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in a Python 3 environment

SAND = '.'
WATER = 'W'
GOLD_COIN = 'G'
COCONUT = 'C'
TREASURE = 'T'
PIRATES = 'P'
ROCK = 'R'
HUT = 'H'
TREE = '*'
BOULDER = 'B'
HOLE = 'O'  # new constant for special spaces in HiddenMap
            # that have already been dug

BLANK = " "
PRESSED_ENTER = ""
MAX_ROWS = 20
MAX_COLUMNS = 50

class MapSizeRecord:
    def __init__(self):
        self.Rows = MAX_ROWS
        self.Columns = MAX_COLUMNS

class PirateRecord:
    def __init__(self):
        self.Row = 0
        self.Column = 0
        self.Score = 100
        self.DigTime = 0.0
        self.TreasureFound = False
        self.NumberOfCoinsFound = 0

def ResetMapSize(MapSize):
    MapSize.Rows = MAX_ROWS
    MapSize.Columns = MAX_COLUMNS
    return MapSize

def ResetMaps(Map, HiddenMap):
    for Row in range (MAX_ROWS):
        for Column in range (MAX_COLUMNS):
            Map[Row][Column] = SAND
            HiddenMap[Row][Column] = SAND

def ResetPirateRecord(Pirate):
    Pirate.Row = 0
    Pirate.Column = 0
    Pirate.Score = 100
    Pirate.DigTime = 0.0
    Pirate.TreasureFound = False
    Pirate.NumberOfCoinsFound = 0

def GenerateMap(Map, MapSize):
    FileIn = open("MapData.txt", 'r')
    DataString = FileIn.readline()
    Data = DataString.split(',')
    MapSize.Rows = int(Data[0])
    MapSize.Columns = int(Data[1])
    for Row in range(MapSize.Rows):
        DataString = FileIn.readline()
        for Column in range(MapSize.Columns):
            Map[Row][Column] = DataString[Column]
    FileIn.close()
    return MapSize

def ProcessDataInputString(Map, DataString):
    Data = DataString.split(',')
    Item = Data[0]
    Row = int(Data[1])
    Column = int(Data[2])
    Map[Row][Column] = Item

def GenerateHiddenMap(HiddenMap):
    FileIn = open("HiddenData.txt", 'r')
    DataString = FileIn.readline()
    while DataString != "":
        ProcessDataInputString(HiddenMap, DataString)
        DataString = FileIn.readline()
    FileIn.close()

def DisplayCompass(Row):
    if Row == 1:
        print()
    elif Row == 2:
        print("          N         ")
    elif Row == 3:
        print("     NW   |   NE    ")
    elif Row == 4:
        print("        \ | /       ")
    elif Row == 5:
        print("   W -----|----- E  ")
    elif Row == 6:
        print("        / | \       ")
    elif Row == 7:
        print("     SW   |   SE    ")
    elif Row == 8:
        print("          S         ")
    else:
        print()

def DisplayMap(Map, MapSize):
    print()
    print("  ", end='')
    for i in range(MapSize.Columns):
        print(i % 10, end='')
    print()
    for Row in range(MapSize.Rows):
        print(f"{Row % 10} ", end='')
        for Column in range(MapSize.Columns):
            print(Map[Row][Column], end='')
        DisplayCompass(Row)
    print()

def FindLandingPlace(Map, MapSize, Pirate):
    Found = False
    Row = 0
    while not Found and Row < MapSize.Rows:
        Column = 0
        while not Found and Column < MapSize.Columns:
            if Map[Row][Column] == 'X':
                Found = True
                Pirate.Row = Row
                Pirate.Column = Column
            Column += 1
        Row += 1
    DisplayMap(Map, MapSize)
    print("X marks the spot where the pirate comes ashore")
    print()

def CheckDistance(Distance):
    ValidDistance = True
    NumberOfSquares = -1
    try:
        NumberOfSquares = int(Distance)
        if NumberOfSquares < 1 or NumberOfSquares > 9:
            print("Distance must be between 1 and 9")
            ValidDistance = False
    except:
        print("Not a valid integer between 1 and 9")
        ValidDistance = False
    return ValidDistance, NumberOfSquares

def CheckDirection(Direction, Row, Column, NumberOfSquares):
    ValidDirection = True
    if Direction == "N":
        Row -= NumberOfSquares
    elif Direction == "NE":
        Row -= NumberOfSquares
        Column += NumberOfSquares
    elif Direction == "E":
        Column += NumberOfSquares
    elif Direction == "SE":
        Row += NumberOfSquares
        Column += NumberOfSquares
    elif Direction == "S":
        Row += NumberOfSquares
    elif Direction == "SW":
        Row += NumberOfSquares
        Column -= NumberOfSquares
    elif Direction == "W":
        Column -= NumberOfSquares
    elif Direction == "NW":
        Row -= NumberOfSquares
        Column -= NumberOfSquares
    else:
        print("Not a valid direction")
        ValidDirection = False
    return ValidDirection, Row, Column

def CheckPath(Map, StartRow, StartColumn, EndRow, EndColumn, Direction):
    ObstacleFound = False
    if Direction == "N":
        for Row in range(EndRow, StartRow):
            if Map[Row][StartColumn] != SAND:
                ObstacleFound = True
    elif Direction == "NE":
        for i in range(1, StartRow - EndRow + 1):
            if Map[StartRow - i][StartColumn + i] != SAND:
                ObstacleFound = True
    elif Direction == "E":
        for Column in range(StartColumn + 1, EndColumn + 1):
            if Map[StartRow][Column] != SAND:
                ObstacleFound = True
    elif Direction == "SE":
        for i in range(1, EndRow - StartRow + 1):
            if Map[StartRow + i][StartColumn + i] != SAND:
                ObstacleFound = True
    elif Direction == "S":
        for Row in range(StartRow + 1, EndRow + 1):
            if Map[Row][StartColumn] != SAND:
                ObstacleFound = True
    elif Direction == "SW":
        for i in range(1, EndRow - StartRow + 1):
            if Map[StartRow + i][StartColumn - i] != SAND:
                ObstacleFound = True
    elif Direction == "W":
        for Column in range(EndColumn, StartColumn):
            if Map[StartRow][Column] != SAND:
                ObstacleFound = True
    elif Direction == "NW":
        for i in range(1, StartRow - EndRow + 1):
            if Map[StartRow - i][StartColumn - i] != SAND:
                ObstacleFound = True
    return ObstacleFound

def Move(Map, MapSize, Pirate, Row, Column):
    if Map[Pirate.Row][Pirate.Column] == PIRATES:
        Map[Pirate.Row][Pirate.Column] = SAND
    Pirate.Row = Row
    Pirate.Column = Column
    Pirate.Score -= 5
    Map[Pirate.Row][Pirate.Column] = PIRATES
    DisplayMap(Map, MapSize)

def PirateWalks(Map, MapSize, HiddenMap, Pirate):
    ObstacleInPath = True
    ValidDistance = False
    ValidDirection = False
    while ObstacleInPath or not ValidDistance or not ValidDirection:
        WalkData = input("Enter length (1 to 9) and direction (N, NE, E, SE, S, SW, W, NW): ")
        Row = Pirate.Row
        Column = Pirate.Column
        ValidDistance, NumberOfSquares = CheckDistance(WalkData[0])
        Direction = WalkData[1:]
        ValidDirection, Row, Column = CheckDirection(Direction, Row, Column, NumberOfSquares)
        if Row >= MapSize.Rows or Column >= MapSize.Columns or Row < 0 or Column < 0:
            ValidDirection = False
            print("Error")
        if ValidDirection:
            ObstacleInPath = CheckPath(Map, Pirate.Row, Pirate.Column, Row, Column, Direction)
            if ObstacleInPath:
                print("Pirate can't walk this way as there is an obstacle in the way")
    Move(Map, MapSize, Pirate, Row, Column)

def DisplayFind(Map, Pirate, ItemFound):
    if ItemFound == COCONUT:
        Item = "Coconut"
        Pirate.Score += 10
        Map[Pirate.Row][Pirate.Column] = COCONUT
    elif ItemFound == TREASURE:
        Item = "Treasure chest"
        Pirate.TreasureFound = True
        Pirate.Score += 200
        Map[Pirate.Row][Pirate.Column] = TREASURE
    elif ItemFound == GOLD_COIN:
        Item = "Gold coin"
        Pirate.NumberOfCoinsFound += 1
        print("The treasure must be nearby")
        Map[Pirate.Row][Pirate.Column] = GOLD_COIN
    else:
        Item = "Unidentified item"
    print(f"Found {Item}")

def PirateDigs(Map, HiddenMap, Pirate):
    HiddenDug = HiddenMap[Pirate.Row][Pirate.Column]
    if HiddenDug not in [SAND, HOLE]:
        DisplayFind(Map, Pirate, HiddenDug)
        # set the dug position to a special "already-dug" character
        HiddenMap[Pirate.Row][Pirate.Column] = HOLE
    elif HiddenDug == HOLE:
        # triggered when digging again in a dug spot
        print("Cannot dig in same spot twice")
    else:
        print("Nothing found")
    if HiddenDug != HOLE:
        # only take away score and time if actually dug
        Pirate.Score -= 10
        Pirate.DigTime += 1.75

def GetPirateAction(Map, MapSize, HiddenMap, Pirate, Answer):
    Answer = input("Pirate to walk (W) or dig (D), to finish game press Enter: ")
    while not (Answer == "W" or Answer == "D" or Answer == PRESSED_ENTER):
        Answer = input("Pirate to walk (W) or dig (D), to finish game press Enter: ")
    if Answer == "W":
        PirateWalks(Map, MapSize, HiddenMap, Pirate)
    elif Answer == "D":
        PirateDigs(Map, HiddenMap, Pirate)
    return Answer

def DisplayResults(Pirate):
    if Pirate.NumberOfCoinsFound > 0:
        print(f"{Pirate.NumberOfCoinsFound} gold coins found")
    print(f"{Pirate.DigTime} hours spent digging")
    print(f"The score is {Pirate.Score}")

def TreasureIsland():
    MapSize = MapSizeRecord()
    Map = [[SAND for i in range(MAX_COLUMNS)] for j in range(MAX_ROWS)]
    HiddenMap = [[SAND for i in range(MAX_COLUMNS)] for j in range(MAX_ROWS)]
    Pirate = PirateRecord()
    MapSize = ResetMapSize(MapSize)
    ResetMaps(Map, HiddenMap)
    MapSize = GenerateMap(Map, MapSize)
    GenerateHiddenMap(HiddenMap)
    ResetPirateRecord(Pirate)
    FindLandingPlace(Map, MapSize, Pirate)
    Answer = BLANK
    while Answer != PRESSED_ENTER and Pirate.Score >= 0 and not Pirate.TreasureFound:
        Answer = GetPirateAction(Map, MapSize, HiddenMap, Pirate, Answer)
    DisplayResults(Pirate)

if __name__ == "__main__":
    TreasureIsland()
    input("Press Enter to finish")
