import itertools

# Part 1: Attempt 1
currentCalibration = 0
input = open("input1.txt", "r")
for line in input:
    currentCalibration += int(line)
print(currentCalibration)

# Part 1: Attempt 2
lines = [int(x) for x in open("input1.txt").readlines()]
print(sum(lines))

# Part 2: Attempt 1
previousCalibrations = []
currentCalibration = 0
switch = True
while switch == True:
    if switch == False:
        break
    # Reset file pointer
    myInput = open("input1.txt", "r")
    for line in myInput:
        # Runs if array is empty
        if not previousCalibrations:
            currentCalibration += int(line)
            previousCalibrations.append(currentCalibration)
        # If array is not empty
        else:
            currentCalibration += int(line)
            print(currentCalibration)
            if previousCalibrations.count(currentCalibration) > 0:
                print("first duplicate value is " + str(currentCalibration))
                switch = False
                break
            else:
                previousCalibrations.append(currentCalibration)

# Part 2: Attempt 2
lines = [int(x) for x in open("input1.txt").readlines()]
currentCalibration = 0
previousCalibrations = set([0])
for line in itertools.cycle(lines):
    currentCalibration += line
    if currentCalibration in previousCalibrations:
        print(currentCalibration)
        break
    previousCalibrations.add(currentCalibration)
