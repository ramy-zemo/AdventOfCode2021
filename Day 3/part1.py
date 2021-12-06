import collections

with open("input.in") as file:
    input_data = [list(x.strip()) for x in file]

done_data = [[] for x in range(len(max(input_data, key=len)))]

for item in input_data:
    for count, number in enumerate(item):
        done_data[count].append(number)

gamma = int("".join([collections.Counter(x).most_common(1)[0][0] for x in done_data]), 2)
epsilon = int("".join([collections.Counter(x).most_common()[-1][0] for x in done_data]), 2)

print(epsilon * gamma)
