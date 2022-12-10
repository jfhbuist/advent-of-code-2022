# day_10_alt.py

def calc_signal_strength(signal_strength, X, cycle):
    offset = 20
    mod = 40
    if (cycle - offset) % mod == 0:
        signal_strength += X*cycle
    return signal_strength

def part_1(input):
    
    cycle = 0
    X = 1
    signal_strength = 0

    with open(input) as f:
        for line in f:
            command = line.strip().split()[0]
            if command == 'addx':
                x = int(line.strip().split()[1])
                cycle += 1
                signal_strength = calc_signal_strength(signal_strength, X, cycle)
                cycle += 1
                signal_strength = calc_signal_strength(signal_strength, X, cycle)
                X += x
            elif command == 'noop':
                cycle += 1
                signal_strength = calc_signal_strength(signal_strength, X, cycle)
    return signal_strength
    

def main(input, part):              

    if part == 0:
        signal_strength = part_1(input)
        return signal_strength
    elif part == 1:
        signal_strength = part_1(input)
        return signal_strength
    elif part == 2:
        return 0


if __name__ == '__main__':
    input = 'input_full/day_10.txt'
    part = 1
    print(main(input, part))
