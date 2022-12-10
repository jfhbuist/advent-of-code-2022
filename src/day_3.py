# day_3.py

def main(input, part):

    alphabet = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
        'A': 27,
        'B': 28,
        'C': 29,
        'D': 30,
        'E': 31,
        'F': 32,
        'G': 33,
        'H': 34,
        'I': 35,
        'J': 36,
        'K': 37,
        'L': 38,
        'M': 39,
        'N': 40,
        'O': 41,
        'P': 42,
        'Q': 43,
        'R': 44,
        'S': 45,
        'T': 46,
        'U': 47,
        'V': 48,
        'W': 49,
        'X': 50,
        'Y': 51,
        'Z': 52,
    }

    # Part 1
    total_priority_1 = 0

    with open(input) as f:
        for line in f:
            line = line.strip()
            comp_1 = line[:int(len(line)/2)]
            comp_2 = line[int(len(line)/2):]
            common = ''.join(set(comp_1).intersection(comp_2))
            total_priority_1 += alphabet[common]

    # Part 2
    total_priority_2 = 0
    elves = ['', '', '']

    with open(input) as f:
        for idx, line in enumerate(f):
            elves[idx % 3] = line.strip()
            if idx % 3 == 2:
                common = ''.join(set(elves[0]).intersection(elves[1], elves[2]))
                total_priority_2 += alphabet[common]

    if part == 0:
        return total_priority_1, total_priority_2
    elif part == 1:
        return total_priority_1
    elif part == 2:
        return total_priority_2


if __name__ == '__main__':
    input = 'input_test/day_3.txt'
    part = 0
    print(main(input, part))
