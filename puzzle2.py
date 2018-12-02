from collections import Counter

# Part 1: Attempt 1
lines = [x for x in open("puzzle2.txt").readlines()]
twoCount = 0
threeCount = 0
for line in lines:
    currentString = list(line)
    currentLetterCount = {}
    for key in currentString:
        if key not in currentLetterCount:
            currentLetterCount[key] = 1
        elif key in currentLetterCount:
            currentLetterCount[key] += 1
    if 3 in currentLetterCount.values():
        threeCount += 1
    if 2 in currentLetterCount.values():
        twoCount += 1
print("Checksum is " + str(twoCount * threeCount))


# Part 1: Attempt 2
lines = [x for x in open("puzzle2.txt").readlines()]
count = [0, 0]
for i in lines:
    currentLine = [j for i, j in Counter(i).most_common()]
    if 3 in currentLine:
        count[0] += 1
    if 2 in currentLine:
        count[1] += 1
print("Checksum is " + str(count[0] * count[1]))

# Part 2: Attempt 1
data = open('puzzle2.txt', 'r')
lines = data.read().strip().splitlines()
data.close()
for i in lines:
    for j in lines:
        diffString = ""
        diffCount = 0
        for index, char in enumerate(i):
            if char != j[index]:
                diffCount += 1
            else:
                diffString += char
        if diffCount == 1:
            print("Same chars are: " + diffString)
            break
