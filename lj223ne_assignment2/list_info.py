from random import randint

lst = []
avg = 0

for i in range(0, 100):
    x = randint(1, 100000)
    lst += [x]

avg = round(sum(lst)/len(lst), 2)

bigNum = max(lst)
lst.remove(bigNum)
scndBigNum = max(lst)
lst += [bigNum]

print("Largest value in list:", bigNum)
print("Smallest value in list:", min(lst))
print("Average value in list:", avg)
print("Second largest value in list:", scndBigNum)
