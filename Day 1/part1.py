with open("input.in") as file:
    input_numbers = [int(x) for x in file.read().split()]

result = 0

for count, i in enumerate(input_numbers[1:]):
    if i > input_numbers[count]:
        result += 1

print(result)
