# coding=utf-8
#20.Factorial Digit Sum
"""n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!"""
def factorial(input):
    still = False
    sum = [1]
    for i in range(1, input + 1):
        for num in range(len(sum) -1, -1, -1):
            sum[num] *= i
            if sum[num] >= 10:
                still = False
                if num == len(sum) - 1:
                    sum.append(sum[num]//10)
                else:
                    sum[num+1] += sum[num]//10
                sum[num] = sum[num] % 10
        while still == False:
            for num in range(len(sum)):
                if sum[num] >= 10:
                    still = False
                    if num == len(sum) - 1:
                        sum.append(sum[num]//10)
                    else:
                        sum[num+1] += sum[num]//10
                    sum[num] = sum[num] % 10
            still = True
    total = 0
    for i in sum:
        total += i
    return total

print factorial(100)