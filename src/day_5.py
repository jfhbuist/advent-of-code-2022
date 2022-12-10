# day_5.py

import copy


def parse_input(input):
    with open(input) as f:
        f_comps = f.read().rstrip('\n').split('\n\n')
        stack_labels = f_comps[0].split('\n').pop().split()
        stack_labels = [int(x)-1 for x in stack_labels]  # convert to integers and shift by 1
        stack_chart = f_comps[0].split('\n')[:-1]
        stacks = [[] for x in stack_labels]
        for layer in reversed(stack_chart):
            for stack in stack_labels:
                position = 1 + stack*4
                if not layer[position].isspace():
                    stacks[stack].append(layer[position])
        # print(stacks)
        instructions = f_comps[1].split('\n')
        return stacks, instructions


def move_1(amount, source, destination, stacks):
    for crate in range(amount):
        stacks[destination].append(stacks[source].pop())


def move_2(amount, source, destination, stacks):
    pickup_stack = stacks[source][-amount:]
    stacks[source] = stacks[source][:-amount]
    stacks[destination] += pickup_stack


def main(input, part):
    stacks, instructions = parse_input(input)

    stacks_1 = stacks  # for part 1
    stacks_2 = copy.deepcopy(stacks)  # for part 2

    for i in instructions:
        amount = int(i.split()[1])
        source = int(i.split()[3])-1
        destination = int(i.split()[5])-1
        move_1(amount, source, destination, stacks_1)
        move_2(amount, source, destination, stacks_2)
        # print(stacks)

    answer_1 = ''
    for s in stacks_1:
        answer_1 += s[-1]

    answer_2 = ''
    for s in stacks_2:
        answer_2 += s[-1]

    if part == 0:
        return answer_1, answer_2
    elif part == 1:
        return answer_1
    elif part == 2:
        return answer_2


if __name__ == '__main__':
    input = 'input_test/day_5.txt'
    part = 0
    print(main(input, part))
