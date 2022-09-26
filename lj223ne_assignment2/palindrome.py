

def is_palindrome(s):
    """Takes a string s and makes it lowercase, converts it into a list
    and removes all spaces, symbols and numbers from the list.
    It then makes a second list in reverse order.
    Lastly compares the normal and reversed list if they are the same.
    returns True if both lists are the same otherwise returns False.
    In short: returns True if provided string is a palindrome"""
    s = s.lower()

    rawstring = [word for word in s]
    string = []
    revString = []

    for i in rawstring:
        if i in "abcdefghijklmnopqrstuvwxyz":
            string += i

    for x in string:
        revString = [x] + revString

    return string == revString


def printRes(p, s):
    if p:
        print(f"{s} is a palindrome.")
    else:
        print(f"{s} is not a palindrome.")


s = "Was it a rat I saw?"
printRes(is_palindrome(s), s)
s = "A nut for a jar of tuna."
printRes(is_palindrome(s), s)
s = "God save the queen!"
printRes(is_palindrome(s), s)
s = "Ni talar bra latin!"
printRes(is_palindrome(s), s)
