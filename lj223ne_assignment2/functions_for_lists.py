
from random import randint


def random_num_list(n):
    lst = [randint(0, 100) for num in range(0, n)]
    return lst


def only_odd(lst):
    oddList = [num for num in lst if num % 2]
    return oddList


def square_lst(lst):
    squareList = [num**2 for num in lst]
    return squareList


def sublist(lst, start, stop):
    subList = lst[start:stop]
    return subList


lst = random_num_list(5)
odds = only_odd(lst)
square = square_lst(lst)
sub = sublist(lst, 1, 4)
print("Here is the list:", lst)
print("Odds in it are:", odds)
print("Let's square each number:", square)
print("Only the three middle values:", sub)
