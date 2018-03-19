#Problem 16. Adding the digits of a large number.

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
#Brainstorm
"""
I will have to make code that simulates an elementary multiplication sequence for each individual number, logs a number
when it can't possibly be altered any further (for example, switching to a new 10's column in the multiplier), and when
the process is finished, adds all the number logs together.
"""
def numSum():
    numlist = []
    bignum = str(2**1000)
    for i in bignum:
        numlist.append(i)
    val = 0
    for x in numlist:
        val = val + int(x)
    return val

print numSum()


