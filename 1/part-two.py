import math
lines = []
list1 = []
list2 = []

with open("input.txt") as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    splits = line.split("   ")
    list1.append(int(splits[0]))
    list2.append(int(splits[1]))

total = sum(x * list2.count(x) for x in list1)


print("Total: ", total)