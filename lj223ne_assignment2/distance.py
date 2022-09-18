from math import sqrt


def distanceCalc(x1, x2, y1, y2):
    d = sqrt((x1-x2)**2 + (y1-y2)**2)
    print(d)
    return round(d, 3)


x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is "
      + f"{distanceCalc(x1, x2, y1, y2)}")
