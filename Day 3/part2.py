import collections

with open("input.in") as file:
    input_data = [x.strip() for x in file]

new_data = input_data.copy()

for c in range(len(input_data[0])):
    how_often = collections.Counter([x[c] for x in new_data]).most_common()

    if how_often[0][1] == how_often[1][1]:
        starting_ = "1"
    else:
        starting_ = str(how_often[0][0]) if how_often[0][1] > how_often[1][1] else str(how_often[1][0])

    new_data = [entry for entry in new_data if entry[c] == starting_]

co2 = int(new_data[0], 2)
new_data = input_data.copy()

for c in range(len(input_data[0])):
    how_often = collections.Counter([x[c] for x in new_data]).most_common()
    if len(how_often) > 1:
        if how_often[0][1] == how_often[1][1]:
            starting_ = "0"
        else:
            starting_ = str(how_often[0][0]) if how_often[0][1] < how_often[1][1] else str(how_often[1][0])

        new_data = [entry for entry in new_data if entry[c] == starting_]

oxy = int(new_data[0], 2)
print(co2 * oxy)
