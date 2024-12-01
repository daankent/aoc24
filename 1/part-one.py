lines = []
list1 = []
list2 = []
with open("input.txt") as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    splits = line.split("   ")
    list1.append( int(splits[0]))
    list2.append(int(splits[1]))

list1.sort()
list2.sort()

total = sum(abs(list1[x]- list2[x]) for x in range(0, 1000))

print("Total: ", total)