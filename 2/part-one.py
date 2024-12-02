lines = []
with open("input.txt") as file:
    lines = file.readlines()

def check_safe(levels):
    gaps = [b - a for a, b in zip(levels, levels[1:])]
    return all([1 <= gap <= 3 for gap in gaps]) or  all([-3 <= gap <= -1 for gap in gaps])

safe_counter = 0

for line in lines:
    levels = [int(x) for x in line.strip().split(" ")]
    
    if check_safe(levels):
        safe_counter += 1
        
print("Safe", safe_counter)