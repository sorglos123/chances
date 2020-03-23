import random

money = 100


# Write your game of chance functions here

def coinFlip(input, bet):
    if bet > money:
        return 'Insufficient funds'
    input = str(input).lower()
    output = ' '
    if input == 'heads' or input == 'tails':
        num = random.randint(1, 2)
        if num == 1:
            output = 'heads'
        elif num == 2:
            output = 'tails'
        if input == output:
            return bet
        elif input != output:
            return bet * (-1)
    else:
        return 'Invalid Input.'


def choHan(input, bet):
    if bet > money:
        return 'Insufficient funds'
    input = str(input).lower()
    output = ' '
    if input == 'odd' or input == 'even':
        sum = (random.randint(1, 6)) + (random.randint(1, 6))
        if sum % 2 == 0:
            output = 'even'
        elif sum % 2 != 0:
            output = 'odd'
        if input == output:
            return bet
        elif input != output:
            return bet * (-1)
    else:
        return 'Invalid Input.'


def drawCard(bet):
    if bet > money:
        return 'Insufficient funds'
    cards = list(range(1, 52))
    drawA = random.randint(1, len(cards))
    a = cards[drawA]
    del cards[drawA]
    drawB = random.randint(1, len(cards))
    b = cards[drawB]
    del cards[drawB]
    if a > b:
        return bet
    else:
        return bet * (-1)


def roulette(input, bet):
    if bet > money:
        return 'Insufficient funds'
    result = random.randint(0, 37)
    print(result)
    red = [1, 3, 5, 7, 9, 12,
           14, 16, 18, 19, 21, 23,
           25, 27, 30, 32, 34, 36]
    black = [2, 4, 6, 8, 10, 11,
             13, 15, 17, 20, 22, 24,
             26, 28, 29, 31, 33, 35]

    if input == result:
        return bet * 35
    elif input == 'Even':
        if result % 2 == 0:
            return bet
        else:
            return bet * (-1)
    elif input == 'Odd':
        if result % 2 != 0:
            return bet
        else:
            return bet * (-1)
    elif input == 'Red':
        if result in red:
            return bet
        else:
            return bet*(-1)
    elif input == 'Black':
        if result in black:
            return bet
        else:
            return bet*(-1)


# Call your game of chance functions here
#print(coinFlip('heads', 10))
#print(choHan('Odd', 5))
#print(drawCard(2))

print(roulette('Odd', 10))