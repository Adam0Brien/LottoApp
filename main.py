import random

userNumbers = []
lotto = []
plus1 = []
plus2 = []
lottoBonus = False
plus1Bonus = False
plus2Bonus = False


def print_hi(name):
    print(f'Hi, {name}')


def checkResults():
    global lottoBonus, plus1Bonus, plus2Bonus
    if lotto[6] in userNumbers:
        print("Bonus Number Found in Lotto")
        lottoBonus = True

    if plus1[6] in userNumbers:
        print("Bonus Number Found in Lotto Plus 1")
        plus1Bonus = True

    if plus2[6] in userNumbers:
        print("Bonus Number Found in Lotto Plus 2")
        plus2Bonus = True



def returnMatches(a, b):
    return list(set(a) & set(b))


def prizeWon(lottoList):
    if len(returnMatches(userNumbers, lottoList)) <= 2:
        print("You've lost")
    if len(returnMatches(userNumbers, lottoList)) == 3:
        print("Congratulations you've won a scratchcard")
    if len(returnMatches(userNumbers, lottoList)) == 4:
        print("You've won a Cash Prize")
    if len(returnMatches(userNumbers, lottoList)) == 5:
        print("You've won a Cash Prize")
    if len(returnMatches(userNumbers, lottoList)) == 6:
        print("You've won the jackpot")


def generateRandomLotto():
    global lotto, plus1, plus2

    print("Generating random numbers")
    lotto = random.sample(range(1, 46), 7)
    print("Lotto):" + str(lotto[0:7]))
    plus1 = random.sample(range(1, 46), 7)
    print("Lotto plus 1):" + str(plus1[0:7]))
    plus2 = random.sample(range(1, 46), 7)
    print("Lotto plus 2):" + str(plus2[0:7]))

    print()
    print()
    mainMenu()


def validateInput(choice, min, max):
    if choice in range(min, max):
        return True
    else:
        return False


def mainMenu():
    print("LOTTO PROGRAM")
    print("1) Generate Random lotto numbers")
    print("2) Enter lotto numbers")
    print("3) Check your results")
    print("4) Exit the program")

    option = int(input("---->"))

    while not validateInput(option, 1, 10):
        option = int(input("---->"))
    if option == 1:
        generateRandomLotto()
    if option == 2:
        userLottoNumbers()
    if option == 3:
        checkWinnings()
    if option == 4:
        exit()
    if option > 4:
        print("Please enter a valid option")
        mainMenu()


def userLottoNumbers():
    global userNumbers
    print("1) Auto generate Numbers")
    print("2) Manually Enter Numbers")

    userNumbers = []
    option = int(input("---->"))

    while not validateInput(option, 1, 3):
        option = int(input("---->"))
    if option == 1:
        userNumbers = (random.sample(range(1, 46), 7))
        print(userNumbers)
        mainMenu()

    if option == 2:
        print("Enter 6 numbers")
        while len(userNumbers) < 6:
            num = int(input("Enter Number -->"))
            while not validateInput(num, 1, 46):
                num = int(input("Enter Number -->"))
            userNumbers.append(num)
            print(userNumbers)
            mainMenu()
        print()
        print()


def checkWinnings():
    print("Which Lotto would you like to check?")
    print("1)  Lotto")
    print("2)  Lotto Plus 1")
    print("3)  Lotto Plus 2")

    option = int(input("---->"))

    while (not validateInput(option, 1, 4)):
        option = int(input("---->"))
    if option == 1:
        print("Comparing user results to Lotto numbers")
        print(returnMatches(userNumbers, lotto))
        prizeWon(lotto)
        mainMenu()
    if option == 2:
        print("Comparing user results to Lotto plus 1 numbers")
        print(returnMatches(userNumbers, plus1))
        prizeWon(plus1)
        mainMenu()
    if option == 3:
        print("Comparing user results to Lotto plus 2 numbers")
        print(returnMatches(userNumbers, plus2))
        prizeWon(plus2)
        mainMenu()



mainMenu()

if __name__ == '__main__':
    # print(lotto)
    print()
    print()
    mainMenu()
