# coding=utf-8
#4. Largest palindrome product
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

#Brainstorm
"""
I will have set a range of numbers from the smallest three digit number (100) to the largest (999). After that, I will
have to multiply each number by itself times a range of numbers equal to itself through the rest of the range. We
will the initial range "range1" and the variable range "rangeX". Each product after multiplying the number in range1 by
the range of rangeX will be tested for being a palindrome. If it is, the palindrom will be logged aloong with its 
factors. At the end, the last palindrome to be logged will be shown along with its factors.

The palindrome test must consider if an odd number of digits reflected across the median point is considered a 
palindrome, or if it is only even numbers of digits. I will create code that logs both styles, and test both.
"""

def paltest(number):
    strnum = str(number)
    midway = len(strnum) / 2
    end = len(strnum)
    for i in range(0, midway):
        test1 = i
        test2 = end - i - 1
        if strnum[test1] != strnum[test2]:
            return False
    return True

palindromes = []

for initial in range(100, 1000):

    for follow in range(initial, 1000):
        case = initial * follow
        if paltest(case):
            palindromes.append(case)
print max(palindromes)


