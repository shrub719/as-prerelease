def PirateDigs(Map, HiddenMap, Pirate):
    if HiddenMap[Pirate.Row][Pirate.Column] != SAND:
        DisplayFind(Map, Pirate, HiddenMap[Pirate.Row][Pirate.Column])
        HiddenMap[Pirate.Row][Pirate.Column] = SAND
    else:
        print("Nothing found")
    Pirate.Score -= 10
    Pirate.DigTime += 1.75