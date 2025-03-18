# Prerelease Notes

## Section C questions

1. 4 marks + 1 screenshot **(5)**
2. 10 marks + 2 screenshots **(12)**
3. 12 marks + 1 screenshot **(13)**

## Potential questions
- can dig up ANY SPACE more than once
- can only walk up to 9 spaces
- score starts at 100, but only lose points through walking
- rock and boulder are separate tiles?
- pirate start position is constant: change spawn point, but keep next to water
- can you go inside the hut (maybe look at the treasure map)
- list reinitialised twice at start
    - change map size
    - make a gameplay loop to try again
        - once score goes to zero
        - unlikely to be after finding treasure unless it changes position (doubt)
- unused parameters
    - `HiddenMap` in `PirateWalks`
    - `Answer` in `GetPirateAction`
- moving any distance costs the same score
- unidentified item in `DisplayFind`
- program breaks if there's no file
- Q2 is likely to include selection logic that requires testing both sides
- `PIRATES` constant is plural?

## Remember
- the pirate's location marker `P` is overwritten when digging,
but the location is kept track of in `PirateRecord`