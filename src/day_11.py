# day_11.py

import math


class Monkey():
    def __init__(self, number, items, op_spec, test, true_target, false_target):
        self.number = number
        self.items = items
        self.op_spec = op_spec
        self.test = test
        self.true_target = true_target
        self.false_target = false_target
        self.inspection_count = 0
        
    def inspect(self, item, part):
        if part == 1: print('  Monkey inspects an item with a worry level of {item:d}.'.format(item=item))
        self.inspection_count += 1
        
    def operation(self, item, part):
        old = item
        if self.op_spec[2] == 'old':
            arg1 = old
        else:
            arg1 = self.op_spec[2]
        if self.op_spec[1] == '*':
            new = old * arg1
            if part == 1: print('    Worry level is multiplied by {a:d}.'.format(a=arg1))
        elif self.op_spec[1] == '+':
            new = old + arg1
            if part == 1: print('    Worry level is increased by {a:d}.'.format(a=arg1))
        elif self.op_spec[1] == '-':
            new = old - arg1
            if part == 1: print('    Worry level is decreased by {a:d}.'.format(a=arg1))      
        return new
    
    def bored(self, item, divisor, part):
        new = item
        if part == 1:
            new = math.floor(new / 3)
            print('    Monkey gets bored with item. Worry level is divided by 3 to {n:d}.'.format(n=new)) 
        # divide by product of all monkey's tests to reduce number without changing flow:
        new = new % divisor
        return new
    
    def find_target(self, item, part):
        test = self.test
        if item % test == 0:
            target = self.true_target
            if part == 1: print('    Current worry level is divisible by {t:d}.'.format(t=test))
        else: 
            target = self.false_target
            if part == 1: print('    Current worry level is not divisible by {t:d}.'.format(t=test))
        if part == 1: print('    Item with worry level {i:d} is thrown to monkey {n:d}.'.format(i=item, n=target)) 
        return target
          
    def main(self, monkey_list, divisor, part):
        for it in self.items:
            self.inspect(it, part)
            it = self.operation(it, part)
            it = self.bored(it, divisor, part)
            target = self.find_target(it, part)
            monkey_list[target].items.append(it)   
        self.items = []  # all items should be thrown out      
            
    def __repr__(self):
        return "Monkey {number:d} (object)".format(number=self.number)


def parse_input(input):
    with open(input) as f:
        monkey_definitions = list(f.read().split('\n\n'))
    monkey_list = []
    for num, md in enumerate(monkey_definitions):
        lines = md.split('\n')
        items = [int(i.strip(',')) for i in lines[1].removeprefix('  Starting items: ').split()]
        op_spec = lines[2].removeprefix('  Operation: new = ').split()
        for i, op in enumerate(op_spec):
            if op.isdigit():
                op_spec[i] = int(op)       
        test = int(lines[3].split()[-1])
        true_target = int(lines[4].split()[-1])
        false_target = int(lines[5].split()[-1])
        m = Monkey(num, items, op_spec, test, true_target, false_target)
        monkey_list.append(m)
    return monkey_list


def monkey_in_the_middle(monkey_list, part, rounds):
    
    divisor = 1    
    for m in monkey_list:
        divisor *= m.test
    
    for r in range(rounds):
        for m in monkey_list:
            if part == 1: print('Monkey {number:d}:'.format(number=m.number))
            m.main(monkey_list, divisor, part)

    inspection_counts = [m.inspection_count for m in monkey_list]
    inspection_counts.sort(reverse=True)
    monkey_business = inspection_counts[0]*inspection_counts[1]
    
    return monkey_business
    

def main(input, part):

    if part == 0:
        monkey_list = parse_input(input)
        monkey_business_1 = monkey_in_the_middle(monkey_list, 1, 20)
        monkey_list = parse_input(input)
        monkey_business_2 = monkey_in_the_middle(monkey_list, 2, 10000)
        return monkey_business_1, monkey_business_2
    elif part == 1:
        monkey_list = parse_input(input)
        monkey_business = monkey_in_the_middle(monkey_list, part, 20)
        return monkey_business
    elif part == 2:
        monkey_list = parse_input(input)
        monkey_business = monkey_in_the_middle(monkey_list, part, 10000)
        return monkey_business


if __name__ == '__main__':
    input = 'input_test/day_11.txt'
    part = 2
    print(main(input, part))
