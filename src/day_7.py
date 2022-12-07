# day_7.py

class Directory():
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        
    def find_child(self, name):
        for c in self.children:
            if c.name == name:
                return c
        return None  # ERROR
    
    def read(self, depth):   
        dir_struct = ''
        dir_format = '- {name} (dir)\n'
        dir_struct += depth*2*' ' + dir_format.format(name=self.name)
        depth += 1
        for c in self.children:
            dir_struct += depth*2*' ' + c.read(depth)
        return(dir_struct)
    
    def __str__(self):
        depth = 0
        return(self.read(depth))
    
    def __repr__(self):
        return "{name} (dir)".format(name=self.name)
    
    def get_size(self):
        size = 0
        for c in self.children:
            size += c.get_size()
        return size
        
       
class File():
    def __init__(self, name, parent, size):
        self.name = name
        self.parent = parent
        self.size = int(size)
    
    def read(self, depth):
        file_format = depth*2*' ' + '- {name} (file, size={size:d})\n'
        output = file_format.format(name=self.name, size=self.size)
        return output
    
    def __str__(self):
        depth = 0
        return(self.read(depth))
    
    def __repr__(self):
        return "{name} (file)".format(name=self.name)
    
    def get_size(self):
        return self.size
       

def parse_input(input):
    with open(input) as f:
        # split file into blocks related to each command (cd or ls),
        # and filter to remove empty strings:
        blocks = list(filter(None, f.read().split('$ ')))
    # collect all directories in a list:
    directory_list = []  
    # collect all files in a list:
    file_list = []  
    # initialize directory structure, assume first line is '$ cd /':
    root = Directory('/', None)
    current_dir = root
    for b in blocks[1:]:  # skip first block, assumed to be '$ cd /'
        lines = b.rstrip('\n').split('\n')
        command_line = lines[0]
        command_line_elements = command_line.split()
        command = command_line_elements[0]
        if command == 'cd': 
            if command_line_elements[1] == '..':
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.find_child(command_line_elements[1])
        elif command == 'ls':
            for l in lines[1:]:
                elements = l.split()
                name = elements[1]
                if elements[0] == 'dir':                  
                    dir = Directory(name, current_dir)
                    current_dir.add_child(dir)     
                    directory_list.append(dir)         
                else:
                    file = File(name, current_dir, elements[0])   
                    current_dir.add_child(file)  
                    file_list.append(file)
    return root, directory_list, file_list


def main(input, part):
    
    root, directory_list, file_list = parse_input(input)

    print(root)
    # print(directory_list)
    # print(file_list)
    
    small_directories = []   
    for dir in directory_list:
        if dir.get_size() <= 100000:
            small_directories.append(dir)
       
    count_1 = 0     
    for dir in small_directories:
        count_1 += dir.get_size()  
       
    free_space = 70000000 - root.get_size()
    required_space = 30000000
    deficient_space = required_space - free_space
    large_directory_sizes = [dir.get_size() for dir in directory_list if dir.get_size() >= deficient_space]    
    count_2 = min(large_directory_sizes)   
    
    if part == 0:
        return count_1, count_2
    elif part == 1:
        return count_1
    elif part == 2:
        return count_2


if __name__ == '__main__':
    input = 'input/day_7_full.txt'
    part = 0
    print(main(input, part))
