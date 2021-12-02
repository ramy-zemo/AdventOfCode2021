with open("input.in") as file:
    input_numbers = [int(x) for x in file.read().split()]

result = 0
# Don't try at home
input_numbers = [x + input_numbers[count + 1] + input_numbers[count + 2] for count, x in enumerate(input_numbers) if count < len(input_numbers) - 2]

for count, i in enumerate(input_numbers[1:]):
    if i > input_numbers[count]:
        result += 1

print(result)
