
def first_last(s):
    return s[0], s[len(s)-1]


def char_types(s):
    string = s.lower()
    v = 0
    c = 0
    for i in string:
        if i in "aeiyou":
            v += 1
        elif i in "bcdfghjklmnpqrstvwxz":
            c += 1
    return v, c


def char_symbol_number(s):
    string = s.lower()
    letters = 0
    nums = 0
    syms = 0
    for i in string:
        if i in "abcdefghijklmnopqrstuvwxyz":
            letters += 1
        elif i in "1234567890":
            nums += 1
        else:
            syms += 1
    return letters, nums, syms


s1 = input("Enter a sentence: ")
s2 = input("Enter another sentence: ")
v, c = char_types(s1)
letters, nums, syms = char_symbol_number(s2)

print(f"First and last in '{s1}': ", first_last(s1))
print(f"In that sentence, the number of vowels is {v} and the number of "
      + f"consonants is {c}")
print(f"In the sentence '{s2}' the number of letters is {letters}, "
      + f"symbols is {syms} and numbers is {nums}")
