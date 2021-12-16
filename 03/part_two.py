# maxpos = 4 # test
maxpos = 11

def filter_common_digit(values, how, pos):
    ones = []
    zeros = []
    for val in values:
        if val & (1 << pos):
            ones.append(val)
        else:
            zeros.append(val)
    if how == 'most':
        if len(ones) >= len(zeros):
            return ones
        else:
            return zeros
    elif how == 'least':
        if len(ones) < len(zeros):
            return ones
        else:
            return zeros


def filter_common(values, how, maxpos):
    comm = filter_common_digit(values, how, maxpos)
    for i in range(maxpos - 1, -1, -1):
        if len(comm) == 1:
            return comm[0]
        comm = filter_common_digit(comm, how, i)
    return comm[0]


values = []
# with open("input-test.txt") as file:
with open("input.txt") as file:
    for line in file:
        values.append(int(line, 2))
oxygen = filter_common(values, 'most', maxpos)
co2 = filter_common(values, 'least', maxpos)
print(f"Oxygen = {oxygen}, CO2 = {co2}.\nLife support ratins is {oxygen * co2}.")
