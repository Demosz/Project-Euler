#Question 1. Finding the sums of multiples below 1000.

"""If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000."""

def multi3():
    threes = []
    val = 3
    while val < 1000:
        threes.append(val)
        val += 3
    return threes

def multi5():
    fives = []
    val = 5
    while val < 1000:
        fives.append(val)
        val += 5
    return fives

def variedsum(ths, fvs):
    all = []
    for i in ths:
        all.append(i)
    for e in fvs:
        if e not in all:
            all.append(e)
    return all

def sum(array):
    total = 0
    for num in array:
        total += num
    return total

print sum(variedsum(multi3(), multi5()))

