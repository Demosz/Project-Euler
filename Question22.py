# coding=utf-8
#22. Names scores
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
 begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
  by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
total = 0
names = ''
alpha = 'abcdefghijklmnopqrstuvwxyz'
with open("p022_names.txt", "r") as f:
    for line in f:
        names += line
nameslist = names.split(',')
for i in range(len(nameslist)):
    nameslist[i] = nameslist[i].replace('\"', '')
nameslist = sorted(nameslist)
print nameslist

for word in range(len(nameslist)):
    wordscore = 0
    for letter in range(len(nameslist[word])):
        char = nameslist[word][letter]
        char = char.lower()
        letterscore = alpha.index(char) + 1
        wordscore += letterscore
    wordscore *= (word + 1)
    total += wordscore

print total