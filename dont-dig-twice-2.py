HOLE = 'O'  # new constant for special spaces in HiddenMap
            # that have already been dug

def DisplayFind(Map, Pirate, ItemFound):
    # removed the already displayed coin/coconut icons when dug
    if ItemFound == COCONUT:
        Item = "Coconut"
        Pirate.Score += 10
    elif ItemFound == TREASURE:
        Item = "Treasure chest"
        Pirate.TreasureFound = True
        Pirate.Score += 200
    elif ItemFound == GOLD_COIN:
        Item = "Gold coin"
        Pirate.NumberOfCoinsFound += 1
        print("The treasure must be nearby")
    else:
        Item = "Unidentified item"
    print(f"Found {Item}")

def PirateDigs(Map, HiddenMap, Pirate):
    HiddenDug = HiddenMap[Pirate.Row][Pirate.Column]
    if HiddenDug not in [SAND, HOLE]:
        DisplayFind(Map, Pirate, HiddenDug)
        # set the dug position to a special "already-dug" character
        HiddenMap[Pirate.Row][Pirate.Column] = HOLE
        # also set it in the actual map
        Map[Pirate.Row][Pirate.Column] = HOLE
    elif HiddenDug == HOLE:
        # triggered when digging again in a dug spot
        print("Cannot dig in same spot twice")
    else:
        print("Nothing found")
        # create hole even if digging sand
        HiddenMap[Pirate.Row][Pirate.Column] = HOLE
        Map[Pirate.Row][Pirate.Column] = HOLE
    if HiddenDug != HOLE:
        # only take away score and time if actually dug
        Pirate.Score -= 10
        Pirate.DigTime += 1.75