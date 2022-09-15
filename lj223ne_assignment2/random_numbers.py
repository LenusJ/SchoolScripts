from random import randint

amount = int(input("Enter number of integers to be generated: "))
minVal = 0
maxVal = 0
numSum = 0
num = 0

print("\nGenerated values:", end=" ")
for i in range(0, amount):
    x = randint(1, 100)
    print(x, end=" ")
    if i == 0:
        minVal = x
        maxVal = x
    if x > maxVal:
        maxVal = x
    if x < minVal:
        minVal = x
    numSum += x

print(f"\nAverage, min, and max are {numSum/amount}, {minVal}, {maxVal}")
