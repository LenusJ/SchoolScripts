from random import randint


def dicecheck(x, one, two, three, four, five, six):
    if x == 1:
        one += 1
        return one
    elif x == 2:
        two += 1
        return two
    elif x == 3:
        three += 1
        return three
    elif x == 4:
        four += 1
        return four
    elif x == 5:
        five += 1
        return five
    elif x == 6:
        six += 1
        return six


roll = 0

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

for i in range(0, 11):
    roll = randint(1, 6)
    dicecheck(roll, one, two, three, four, five, six)

print(one, two, three, four, five, six)
