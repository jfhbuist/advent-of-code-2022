# day_9.py

import math


def move_head(head_pos, instruction):
    if instruction[0] == 'R':
        head_pos[0] += 1
    elif instruction[0] == 'L':
        head_pos[0] -= 1
    elif instruction[0] == 'U':
        head_pos[1] += 1
    elif instruction[0] == 'D':
        head_pos[1] -= 1
    else:
        raise Exception("Instruction not understood")
    return head_pos


def move_knot(lead_pos, knot_pos):
    x_diff = lead_pos[0] - knot_pos[0]
    y_diff = lead_pos[1] - knot_pos[1]
    # diff = [head_pos[i] - tail_pos[i] for i in range(len(head_pos))]
    # check_diff = [abs(c) > 1 for c in diff]
    # if any(check_diff):
    if abs(x_diff) > 1:
        # we need to move
        knot_pos[0] += int(math.copysign(1,x_diff))
        if abs(y_diff) >= 1:
            # we need a diagonal move
            knot_pos[1] += int(math.copysign(1,y_diff))
    elif abs(y_diff) > 1:
        # we need to move
        knot_pos[1] += int(math.copysign(1,y_diff))
        if abs(x_diff) >= 1:
            # we need a diagonal move
            knot_pos[0] += int(math.copysign(1,x_diff))
    return knot_pos


def rope_bridge(input, head_pos, knots):
    
    number_of_knots = len(knots)
    tail_pos = knots[number_of_knots]
    visited = {tuple(tail_pos): 1}
    
    with open(input) as f:
        for line in f:
            instruction = line.strip().split()
            instruction[1] = int(instruction[1])
            # print(instruction)
            for step in range(instruction[1]):
                head_pos = move_head(head_pos, instruction)
                lead_pos = head_pos
                for k in knots:
                    knots[k] = move_knot(lead_pos, knots[k])
                    lead_pos = knots[k]
                tail_pos = knots[number_of_knots]
                visited[tuple(tail_pos)] = 1
                # print(head_pos, tail_pos)
    number_visited = len(visited)
    return number_visited


def main(input, part):
    
    if part == 0:
        # starting position
        x = 0
        y = 0
        head_pos = [x, y]
        knots = {1: [x,y]}
    
        number_visited_1 = rope_bridge(input, head_pos, knots)
        
        # starting position
        x = 0
        y = 0
        head_pos = [x, y]
        knots = {
            1: [x, y],
            2: [x, y],
            3: [x, y],
            4: [x, y],
            5: [x, y],
            6: [x, y],
            7: [x, y],
            8: [x, y],
            9: [x, y],
        }    
        number_visited_2 = rope_bridge(input, head_pos, knots)

        return number_visited_1, number_visited_2
    elif part == 1:
        # starting position
        x = 0
        y = 0
        head_pos = [x, y]
        knots = {1: [x,y]}
    
        number_visited_1 = rope_bridge(input, head_pos, knots)

        return number_visited_1
    elif part == 2:
        # starting position
        x = 0
        y = 0
        head_pos = [x, y]
        knots = {
            1: [x, y],
            2: [x, y],
            3: [x, y],
            4: [x, y],
            5: [x, y],
            6: [x, y],
            7: [x, y],
            8: [x, y],
            9: [x, y],
        }    
        number_visited_2 = rope_bridge(input, head_pos, knots)

        return number_visited_2


if __name__ == '__main__':
    input = 'input/day_9_full.txt'
    part = 0
    print(main(input, part))
