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