
def get_abcd(a, b, c, d):
    a = a * 1000
    b = b * 100
    c = c * 10
    return a + b + c + d


def get_dcba(a, b, c, d):
    d = d * 1000
    c = c * 100
    b = b * 10
    return d + c + b + a


numFound = 0
a = 0
b = 0
c = 0
d = 0

for i in range(1, 10):
    if numFound == 1:
        break
    a = i
    for j in range(0, 10):
        if numFound == 1:
            break
        b = j
        for h in range(0, 10):
            if numFound == 1:
                break
            c = h
            for k in range(1, 10):
                d = k
                if get_abcd(a, b, c, d)*4 == (get_dcba(a, b, c, d)):
                    numFound = 1
                    break

print(f"The number {get_dcba(a, b, c, d)} is 4 times greaster than"
      + f" {get_abcd(a, b, c, d)}")
