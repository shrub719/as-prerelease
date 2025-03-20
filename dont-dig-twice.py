HOLE = 'O'  # new constant for special spaces in HiddenMap
            # that have already been dug

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