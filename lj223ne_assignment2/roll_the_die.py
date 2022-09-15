from random import randint


""" Calculates the difference between biggest and smallest number
then returns the value as a percent """


def diffCalc(biggest, smallest):
    decNum = (biggest - smallest) / biggest
    percent = decNum * 100
    return percent


roll = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
rollAmount = 10

""" Checks the average 20 times with each time the dice is being rolled 2 as
many as the last time
then store the number of times a certain face has been rolled in variables
after that check which is the biggest and smallest and send it to the function
diffCalc lastly print the results. """
for j in range(0, 21):
    for i in range(0, rollAmount + 1):
        roll = randint(1, 6)
        if roll == 1:
            one += 1
        elif roll == 2:
            two += 1
        elif roll == 3:
            three += 1
        elif roll == 4:
            four += 1
        elif roll == 5:
            five += 1
        elif roll == 6:
            six += 1
    bigNum = max(one, two, three, four, five, six)
    smallNum = min(one, two, three, four, five, six)
    perc = diffCalc(bigNum, smallNum)
    print(f"For {rollAmount} rolls, the difference is {round(perc, 2)}%")
    rollAmount *= 2
