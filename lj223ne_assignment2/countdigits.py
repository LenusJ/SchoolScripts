
numIn = int(input("Enter a large positive integer: "))

odd = 0
even = 0
zero = 0

if numIn > 0:
    x = [int(num) for num in str(numIn)]
    
    for i in x:
        if i == 0:
            zero += 1
        elif i % 2:
            odd += 1
        elif i % 2 == 0:
            even += 1
    print("Zeros:", zero)
    print("Odd:", odd)
    print("Even:", even)
else:
    print("Error: Not a positive int!")
