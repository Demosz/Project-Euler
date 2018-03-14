nums = []
with open("Problem13numbers.txt", "r") as f:
    for line in f:
        nums.append(line)

total = 0
for i in nums:
    total += int(i)
print str(total)[:10]
