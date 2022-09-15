numIn = int(input("Enter a positive integer: "))
k = 0
count = 0

if numIn >= 0:
    while count < numIn:
        k += 2
        count += k
    print(f"{k - 2} is the largest k such that 0+2+4+6...+k < {numIn}")
else:
    print("Input error!")
