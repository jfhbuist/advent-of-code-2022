# day_1.py

def sort_calories(current_cal, elf_idx, max_cal, max_idx):
    for pos, cal in enumerate(max_cal):
        if current_cal > cal:
            # shift entries right and insert removed value at current position
            max_cal.insert(pos, max_cal.pop())
            max_idx.insert(pos, max_idx.pop())
            # replace inserted value with new current cal value
            max_cal[pos] = current_cal
            max_idx[pos] = elf_idx
            break
    return max_cal, max_idx


def main(input, part):
    current_cal = 0
    elf_idx = 0
    max_cal = [0, 0, 0]  # first is highest
    max_idx = [0, 0, 0]  # first is highest

    with open(input) as f:
        for line in f:
            if line == '\n':
                max_cal, max_idx = sort_calories(current_cal, elf_idx, max_cal, max_idx)
                current_cal = 0
                elf_idx += 1
                # print(line.strip())
            else:
                item_cal = int(line.strip())
                current_cal += item_cal
                # print(number)
    # when done with looping through file, check if anything still needs to be added
    if current_cal != 0:
        max_cal, max_idx = sort_calories(current_cal, elf_idx, max_cal, max_idx)
        current_cal = 0
        elf_idx += 1

    max_idx = list(x+1 for x in max_idx)  # for indexing convention starting from 1

    if part == 0:
        return max_cal[0], sum(max_cal)
    elif part == 1:
        return max_cal[0]
    elif part == 2:
        return sum(max_cal)


if __name__ == '__main__':
    input = 'input/day_1_test.txt'
    part = 0
    print(main(input, part))
