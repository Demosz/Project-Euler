# coding=utf-8
#25. 1000-digit Fibonacci number.
"""The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""

base = [[1], [1]]

lastval = base[len(base) - 1]
lastval2 = base[len(base) - 2]
fnd = False

while fnd == False:
    newval = []
    lastval = base[len(base) - 1]
    lastval2 = base[len(base) - 2]
    if len(str(lastval)) > len(str(lastval2)):
        lastval2.append(0)
    temp = list(lastval)
    temp2 = list(lastval2)
    for i in range(len(lastval)):
        next = temp[i] + temp2[i]
        if next > 9:
            if i == (len(lastval) - 1):
                newval.append(next % 10)
                newval.append(next // 10)
            else:
                newval.append(next % 10)
                temp[i+1] += (next // 10)
        else:
            newval.append(next)
    base.append(newval)
    print len(base)
    dist = len(newval)
    if dist == 1000:
        fnd = True
print base[len(base)-1]
print len(base)
