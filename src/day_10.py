# day_10.py

def parse_input(input):
    instructions = []
    with open(input) as f:
        for line in f:
            command = line.strip().split()[0]
            if command == 'addx':
                x = int(line.strip().split()[1])
                instruction = [command, x]
            elif command == 'noop':
                instruction = [command]
            instructions.append(instruction)      
    return instructions


def calc_signal_strength(cycle, X, row_width):
    offset = row_width/2
    if (cycle - offset) % row_width == 0:
        signal_strength = X*cycle
    else:
        signal_strength = 0
    return signal_strength

            
def evaluate_pixel(p, X):
    # sprite location:
    sprite = [X-1, X, X+1]
    if p in sprite:
        pixel = 1
    else:
        pixel = 0
    return pixel


def render_image(pixels):
    image = ''
    legend = {0: '.', 1: '#'}
    for row in pixels:
        for p in row:
            image += legend[p]
        image += '\n'
    return image
  

def main(input, part): 
    
    instructions = parse_input(input)  
    
    cycle = 1
    X = 1  
    instr_number = 0
    instr_total = len(instructions)
    wait = 0
    row_width = 40
    row_total = 6
    pixel_total = row_width*row_total
    
    signal_strength = 0
    pixels = [[0] * row_width for r in range(row_total)]
    
    for row in range(row_total):
        for p in range(row_width):
            signal_strength += calc_signal_strength(cycle, X, row_width)
            pixels[row][p] = evaluate_pixel(p, X)
            instr = instructions[instr_number]
            # print(cycle, p, pixels[p], X)
            if instr[0] == 'addx':
                if wait == 0:  # we are not waiting for execution, so begin operation
                    x = instr[1]
                    wait = 1  # we are now waiting
                elif wait == 1:  # we have been waiting for execution, so finish operation now
                    X += x
                    wait = 0  # we are not waiting anymore
                    instr_number += 1  # continue with next operation               
            elif instr[0] == 'noop':
                instr_number += 1
            cycle += 1

        
    image = render_image(pixels).rstrip('\n')  # BPJAZGAP

    if part == 0:       
        return signal_strength, image
    elif part == 1:      
        return signal_strength
    elif part == 2:
        return image


if __name__ == '__main__':
    input = 'input_test/day_10.txt'
    part = 2
    ans = main(input, part)
    print(ans)
