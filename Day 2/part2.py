horizontal = 0
depth = 0
aim = 0

with open("input.in") as file:
    input_data = [(x.replace("\n", "").split()[0], int(x.replace("\n", "").split()[1])) for x in file.readlines()]

for command, step in input_data:
    if command == "forward":
        horizontal += step
        depth += aim * step
    elif command == "up":
        aim -= step
    elif command == "down":
        aim += step

print(horizontal * depth)
