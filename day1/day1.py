file = open("day1input.txt", "r")

elves = {"0": []}
elfIndex = 0

# Run through the different lines and create a dictionary with {[Elf]:[Snacks]}
for line in file.readlines():
    lineStripped = line.strip("\n")
    if lineStripped == "":
        elfIndex += 1
        elves[str(elfIndex)]=[]
    else:
        elves[str(elfIndex)].append(lineStripped)

sumList = []
for elfIterator in elves.keys():
    sum = 0
    for calories in elves[elfIterator]:
        sum += int(calories)
    sumList.append(sum)
sumList.sort()
totalCalorieCount = 0
for i in range(3):
    totalCalorieCount += sumList.pop()
print(totalCalorieCount)

file.close()
