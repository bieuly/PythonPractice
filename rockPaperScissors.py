import random

choices = [("r", "rock"), ("p", "paper"), ("s", "scissors")]

randomTaunts = ["get WRECKED!", "HAHA", "don't cry it'll be over soon", "suck it!",
                "too predictable", "tsk tsk", "c'mon man atleast make it hard for me"]

points = {
    "human": 0,
    "cpu": 0
}

humanName = ""


def startGame(num_of_points_to_win):
    while(not isGameDone()):
        humanChoice = getHumanChoice()
        cpuChoice = generateCpuChoice()
        playRound(humanChoice, cpuChoice)
        if(isGameDone()):
            print("Final Score: {} {}   Computer {}".format(humanName,
                                                            points["human"], points["cpu"]))
        else:
            print("Score: {} {}   Computer {}".format(humanName,
                                                      points["human"], points["cpu"]))


def isGameDone():
    if((points["human"] == num_of_points_to_win) or (points["cpu"] == num_of_points_to_win)):
        return True
    else:
        return False


def isValidChoice(input):
    choice = input.lower()
    if((choice == "r") or (choice == "p") or (choice == "s")):
        return True
    else:
        return False


def getHumanChoice():
    gotValidChoice = False
    humanInput = ""
    while(not gotValidChoice):
        humanInput = input("\nChoose (R)ock, (P)aper, or (S)cissors? ").lower()
        if(isValidChoice(humanInput)):
            gotValidChoice = True
        else:
            print("Please choose a valid choice: (R)ock, (P)aper, or (S)cissors")
    return interpretHumanChoice(humanInput)


def interpretHumanChoice(humanInput):
    for i in range(len(choices)):
        currentChoice = choices[i]
        if currentChoice[0] == humanInput:
            return choices[i]


def generateCpuChoice():
    choiceIndex = random.randint(0, 2)
    return choices[choiceIndex]


def playRound(humanChoice, cpuChoice):
    winner = ""
    winner = decideWinner(humanChoice[0], cpuChoice[0])
    if(winner):
        addPoint(winner)
        winnerName = ""
        if(winner == "human"):
            winnerName = humanName
        else:
            winnerName = "Computer"

        print("{}: {}\t Computer: {}\t {} wins!\n".format(humanName,
                                                          humanChoice[1], cpuChoice[1], winnerName))
        if(winner == "cpu"):
            taunt()
    else:
        print("{}: {}\t Computer: {}\t A draw\n".format(humanName,
                                                        humanChoice[1], cpuChoice[1]))


def taunt():
    taunt = randomTaunts[random.randint(0, len(randomTaunts)-1)]
    print("cpu says: {}\n".format(taunt))


def decideWinner(human, cpu):
    if(human == cpu):
        return ""
    if((human == "r" and cpu == "s") or (human == "p" and cpu == "r") or (human == "s" and cpu == "p")):
        return "human"
    else:
        return "cpu"


def addPoint(winner):
    currentPoints = points[winner]
    points[winner] = currentPoints + 1


def isValidNumber(userInput):
    try:
        number = int(userInput)
        if(number > 0):
            return True
        else:
            return False
    except ValueError:
        return False


def getNumberOfPointsRequiredToWin():
    gotValidNumber = False
    userInput = ""
    while(not gotValidNumber):
        userInput = input("How many points are required for a win? ")
        if(isValidNumber(userInput)):
            gotValidNumber = True
        else:
            print("Please enter a positive integer greater than 0!\n")
    return int(userInput)


print("Welcome to Rock, Paper, Scissors!\n")
humanName = input("What is your name? ")
num_of_points_to_win = getNumberOfPointsRequiredToWin()

startGame(num_of_points_to_win)
