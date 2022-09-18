from random import randint


def pronoun(x):
    i = randint(1, 5)
    if i == 1:
        x = "I"
    if i == 2:
        x = "You"
    if i == 3:
        x = "It"
    if i == 4:
        x = "We"
    if i == 5:
        x = "They"
    return x


def verb(x):
    i = randint(1, 5)
    if i == 1:
        x = "will eat"
    if i == 2:
        x = "will touch"
    if i == 3:
        x = "will see"
    if i == 4:
        x = "will pull"
    if i == 5:
        x = "will throw"
    return x


def noun(x):
    i = randint(1, 5)
    if i == 1:
        x = "a house"
    if i == 2:
        x = "a tree"
    if i == 3:
        x = "a car"
    if i == 4:
        x = "a computer"
    if i == 5:
        x = "a ball"
    return x


p = ""
v = ""
n = ""

print(pronoun(p), verb(v), noun(n))
