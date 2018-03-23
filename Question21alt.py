# coding=utf-8
#21. Amicable Numbers
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

class Amic:
    def __init__(self, num):
        self.amicList2 = []
        self.total = self.listAll2(num)

    #This method returns all the factors of a given number, without the given number.

    def factors(self, x):
        result = []
        i = 1
        while i*i <= x:
            if x % i == 0:
                result.append(i)
                if x/i != i:
                    result.append(x/i)
            i += 1
        result = sorted(result)
        try:
            result.pop()
        except:
            return
        return result

    #This method sums the factors of a given number without the given number as part of the sum.

    def factorSum(self, numList):
        total = 0
        try:
            for i in numList:
                total += i
        except:
            return
        return total

    #This method determines if a given amicable number is acceptable given the paramaters of the problem (below 10000).

    def idAmicable2(self, num): #a
        facs = self.factors(num)
        sum = self.factorSum(facs) #b
        facs2 = self.factors(sum) #factors of b
        sum2 = self.factorSum(facs2) # test to see if a
        if num < 10000 and sum < 10000:
            if sum2 == num and num != sum:
                if num not in self.amicList2:
                    self.amicList2.append(num)
                if sum not in self.amicList2:
                    self.amicList2.append(sum)

    #This last function returns the sum of all amicable numbers under the given value.

    def listAll2(self, val):
        total = 0
        for i in range(1, val+1):
            self.idAmicable2(i)
        for x in self.amicList2:
            total += x
        return total

a = Amic(10000)
print a.total