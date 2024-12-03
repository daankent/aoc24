import re
memory = ""

with open("input.txt") as file:
    memory = file.read()
    
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
total = sum([(int(instruction[0])*int(instruction[1])) for instruction in re.findall(pattern, memory)])
print(total)