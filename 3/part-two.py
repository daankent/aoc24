import re
memory = ""

with open("input.txt") as file:
    memory = file.read()

pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

disabled = False
i = 0
total = 0
while i < len(memory):
    if memory[i:i+4] == "do()":
            disabled = False
            i += 4
    elif memory[i:i+7] == "don't()":
            disabled = True
            i += 7
    if memory[i:i+4] == "mul(":
        check = pattern.match(memory, i)
        if check and not disabled:
            x, y = check.groups()
            total += int(x) * int(y)
            i = check.end()
        else:
            i += 4
    else: i += 1
print(total)