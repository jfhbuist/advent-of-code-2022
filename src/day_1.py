# day_1.py

input = 'input/day_1_full.txt'

current_cal = 0
elf_idx = 0
max_cal = [0, 0, 0]  # first is highest
max_idx = [0, 0, 0]  # first is highest

with open(input) as f:
    for line in f:
        if line == '\n':
            for pos, cal in enumerate(max_cal):
                if current_cal > cal:
                    # shift entries right and insert removed value at current position
                    max_cal.insert(pos, max_cal.pop())
                    max_idx.insert(pos, max_idx.pop())
                    # replace inserted value with new current cal value
                    max_cal[pos] = current_cal
                    max_idx[pos] = elf_idx
                    break
            current_cal = 0
            elf_idx += 1
            # print(line.strip())
        else:
            item_cal = int(line.strip())
            current_cal += item_cal
            # print(number)

print(max_cal)
print(sum(max_cal))
max_idx = list(x+1 for x in max_idx)  # for indexing convention starting from 1
print(max_idx)
