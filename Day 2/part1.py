horizontal = 0
depth = 0

with open("input.in") as file:
    input_data = [(x.replace("\n", "").split()[0], int(x.replace("\n", "").split()[1])) for x in file.readlines()]

for command, step in input_data:
    if command == "forward":
        horizontal += step
    elif command == "up":
        depth -= step
    elif command == "down":
        depth += step

print(horizontal * depth)
