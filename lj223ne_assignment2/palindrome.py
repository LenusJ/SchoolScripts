

def is_palindrome(s):
    """Takes a string s and makes it lowercase, converts it into a list
    and removes all spaces, symbols and numbers from the list.
    It then makes a second list in reverse order.
    Lastly compares the normal and reversed list if they are the same
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

    if string == revString:
        palindrome = True
    else:
        palindrome = False

    return palindrome


s = input("Enter a palindrome: ")

palindrome = is_palindrome(s)
if palindrome:
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")
