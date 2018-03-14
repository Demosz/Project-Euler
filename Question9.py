import math

a = 0
b = 0
c = 0
fnd = False

while fnd is False:
    for i in range(a + 1):
        b = i
        x = ((a ** 2) + (b ** 2))
        print x
        c = math.sqrt(x)
        print a, b, c
        print a + b + c, "!"
        if a + b + c == 1000:
            fnd = True
            break
        else:
            continue
    if fnd == False:
        a += 1
        b = 0
        c = 0
    elif fnd == True:
        print a * b * c
        print "!!!"
