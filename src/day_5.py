# day_5.py

input = 'input/day_5_full.txt'


def move_part_1(amount, source, destination, stacks):
    for container in range(amount):
        stacks[destination].append(stacks[source].pop())


def move_part_2(amount, source, destination, stacks):
    pickup_stack = stacks[source][-amount:]
    stacks[source] = stacks[source][:-amount]
    stacks[destination] += pickup_stack


with open(input) as f:
    f_comps = f.read().split('\n\n')
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
    for i in instructions:
        amount = int(i.split()[1])
        source = int(i.split()[3])-1
        destination = int(i.split()[5])-1
        move_part_2(amount, source, destination, stacks)
        # print(stacks)

    answer = ''
    for s in stacks:
        answer += s[-1]
    print(answer)
