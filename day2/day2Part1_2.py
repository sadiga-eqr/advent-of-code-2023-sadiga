
import re

redCount = 12
greenCount = 13
blueCount = 14

def getColors(s):
    pattern = r"(red|green|blue)"
    return re.search(pattern, s)[0]

def parseLine(inputLine):
    game, data = inputLine.split(":")

    #Get game number 1st number
    patternNum = r"\d+"
    game_num = int(re.search(patternNum, game)[0])

    values = data.split(";")
    subsets = []

    for value in values:
        colorsData = {"red" : 0, "green" : 0, "blue" : 0,}
        parts = value.split(",")
        for part in parts:
            colorsData[getColors(part)] = int(re.search(patternNum, part)[0])
            subsets.append(colorsData)

    return game_num, subsets


#Part1
def isValidGame(subsets: list[dict[str, int]]):
    for subset in subsets:
        if subset["red"] > redCount or subset["green"] > greenCount or subset["blue"] > blueCount:
            return False
    return True

#Part2 
def calculatePower(subsets):
    red = 0
    green = 0
    blue = 0
    for subset in subsets:
        red = max(red, subset["red"])
        green = max(green, subset["green"])
        blue = max(blue, subset["blue"])
    return red * green * blue

total = 0 
# Open the file in read mode
with open('day2Input.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        game_number, subsets = parseLine(line)
          #if isValidGame(subsets):
            #total += game_number
        total += calculatePower(subsets)
    
    print(f"Total  = {total}")