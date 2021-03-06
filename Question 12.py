#Question 12. Factors of Tri-Numbers
"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

#This function finds the value of the Xth Tri-Number
def triNumber(X):
    total = 0
    for i in range(1, X + 1):
        total = total + i
    return total

#This function determines all the factors, sorted, of a given number
def factors(x):
    result = []
    i = 1
    while i*i <= x:
        if x % i == 0:
            result.append(i)
            if x/i != i:
                result.append(x/i)
        i += 1
    return sorted(result)

#This Function takes a given Tri-Number value and factors it. If it doesn't have enough factors, the next Tri is called
def findNthTri():
    start = 1
    fnd = False
    while fnd == False:
        facs = factors(triNumber(start))
        if len(facs) > 501:
            fnd = True
        else:
            start += 1
    print triNumber(start)

findNthTri()

