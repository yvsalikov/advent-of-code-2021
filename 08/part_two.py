# Advent of Code 2021
# https://adventofcode.com/2021
# Day 8: Seven Segment Search

#  0(6):   1(2):   2(5):   3(5):   4(4):
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....
#
#  5(5):   6(6):   7(3):   8(7):   9(6):
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg



def get_segment_with_brightness(patterns, lengths, brightness):
    # print(f"\tget_segment_with_brightness")
    group = []
    for p in patterns:
        if len(p) in lengths:
            group.append(p)
    # print(f"\t{group}")
    
    illuminated = {}
    for digit in group:
        for segment in digit:
            if segment not in illuminated:
                illuminated[segment] = 1
            else:
                illuminated[segment] += 1
    
    for k,v in illuminated.items():
        if v == brightness:
            # print(f"\t {k} -> {v}")
            return k
    else:
        return "z"


def translate(corrupted_digit, translation):
    translated = ""
    for s in corrupted_digit:
        translated += translation[s]
    return sorted(translated)

output_value = 0
with open("input.txt") as file:
    for line in file:
        pattern, output = line.rstrip().split(" | ", 2)
        patterns = pattern.split() #[set(d) for d in pattern.split()]
        # s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        # d0 = [1, 1, 1, 0, 1, 1, 1] ###
        # d1 = [0, 0, 1, 0, 0, 1, 0]
        # d2 = [1, 0, 1, 1, 1, 0, 1] #
        # d3 = [1, 0, 1, 1, 0, 1, 1] #
        # d4 = [0, 1, 1, 1, 0, 1, 0]
        # d5 = [1, 1, 0, 1, 0, 1, 1] #
        # d6 = [1, 1, 0, 1, 1, 1, 1] ###
        # d7 = [1, 0, 1, 0, 0, 1, 0]
        # d8 = [1, 1, 1, 1, 1, 1, 1]
        # d9 = [1, 1, 1, 1, 0, 1, 1] ###
        # print([sum(x) for x in zip(d0, d1, d2, d3, d4, d5, d6, d7, d8, d9)])
        # print([sum(x) for x in zip(d1, d7, d2, d3, d5, d0, d6, d9)])
        
        translation = {}
        translation[get_segment_with_brightness(patterns, [2, 3], 1)] = "a"
        translation[get_segment_with_brightness(patterns, [2, 4, 5], 1)] = "e"
        translation[get_segment_with_brightness(patterns, [2, 4, 5], 2)] = "b"
        translation[get_segment_with_brightness(patterns, [2, 3, 5, 6], 5)] = "d"
        translation[get_segment_with_brightness(patterns, [2, 3, 4, 5], 3)] = "g"
        translation[get_segment_with_brightness(patterns, [2, 3, 4, 5, 6, 7], 9)] = "f"
        for p in patterns:
            if len(p) == 7:
                for s in p:
                    if s not in translation:
                        translation[s] = "c"
                        break
        # print(translation)
        
        output_digits = output.split()
        output_char = ""
        for digit in output_digits:
            length = len(digit)
            if length == 2:
                output_char += "1"
            elif length == 3:
                output_char += "7"
            elif length == 4:
                output_char += "4"
            elif length == 7:
                output_char += "8"
            elif length == 5:
                correct = translate(digit, translation)
                if "e" in correct:
                    output_char += "2"
                elif "b" in correct:
                    output_char += "5"
                else:
                    output_char += "3"
            else: # length == 6
                correct = translate(digit, translation)
                if "d" not in correct:
                    output_char += "0"
                elif "c" not in correct:
                    output_char += "6"
                else:
                    output_char += "9"
        output_value += int(output_char)
print(f"Sum of output values is {output_value}")
