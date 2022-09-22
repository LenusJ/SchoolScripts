
numIn = int(input("Enter a large positive integer: "))

odd = 0
even = 0
zero = 0

if numIn > 0:
    for i in str(numIn):
        if i in "0":
            zero += 1
        elif i in "13579":
            odd += 1
        elif i in "2468":
            even += 1

    print("Zeros:", zero)
    print("Odd:", odd)
    print("Even:", even)

else:
    print("Error: Not a positive int!")
