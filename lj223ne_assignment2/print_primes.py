amount = int(input("How many primes? "))
lineCount = 1
n = 2

while amount > 0:  # While the amount of primes printed hasnt reached zero
    primeCheck = True
    for i in range(2, n):
        if n % i == 0:
            primeCheck = False  # code taken from the iterations presentation
    if primeCheck:  # If it found a prime do this
        if lineCount < 10:  # Primes printed per a line, increase when printed
            print(n, end=" ")
            lineCount += 1
        elif lineCount == 10:  # if 10 reset to 1 and print n on new line
            print(n)
            lineCount = 1
        amount -= 1  # A prime has been printed
        n += 1
    else:  # Just to increase the n value for the next number to be checked
        n += 1
