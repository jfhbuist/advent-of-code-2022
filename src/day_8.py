# day_8.py

import numpy as np

def parse_input(input):
    with open(input) as f:
        # initialize numpy array
        trees = np.array([[int(t) for t in list(f.readline().strip())]])      
        # add each line to array 
        for line in f:
            trees = np.append(trees, [[int(t) for t in list(line.strip())]], axis=0)
        
    return trees

def check_view(t, possible_trees):
    # Which tree (if any) blocks our view?
    blocker = np.where(possible_trees>=t)[0]
    if blocker.size > 0:  # check if there is a blocker
        # Index of blocker is the number of trees between blocker and the current tree.
        # So the number of trees we see is blocker + 1.
        count = blocker[0] + 1                   
    else:
        # If there is no blocker, we see all possible trees:
        count = possible_trees.size
    return count


def main(input, part):

    trees = parse_input(input)
    inner_trees = trees[1:-1,1:-1]
    
    ### Part 1
    
    width, height = trees.shape 
    # Which trees are visible?
    visible = np.zeros((width, height), dtype=int)   
    # Outer trees are all visible
    visible[0,:] = 1
    visible[-1,:] = 1
    visible[:,0] = 1
    visible[:,-1] = 1
    
    # Loop over inner trees from left, right, top, and bottom. If tree is visible from any side, 
    # it is visible.
    
    # left pass
    for i, row in enumerate(inner_trees):
        for j, t in enumerate(row):
            if (t - max(trees[i+1,:j+1])) > 0:
                visible[i+1, j+1] = 1
    
    # right pass
    for i, row in reversed(list(enumerate(inner_trees))):
        for j, t in reversed(list(enumerate(row))):
            if (t - max(trees[i+1,j+2:])) > 0:
                visible[i+1, j+1] = 1
    
    # top pass
    for j, col in enumerate(inner_trees.T):
        for i, t in enumerate(col):
            if (t - max(trees[:i+1,j+1])) > 0:
                visible[i+1, j+1] = 1
    
    # bottom pass
    for j, col in enumerate(inner_trees.T):
        for i, t in enumerate(col):
            if (t - max(trees[i+2:,j+1])) > 0:
                visible[i+1, j+1] = 1
    
    total_visible = np.sum(visible)
      
    ### Part 2
    
    # Initialize score for each tree. Outer trees have score of zero.
    score = np.zeros((width, height), dtype=int)
    
    # Loop over inner trees
    for i, row in enumerate(inner_trees):  
        for j, t in enumerate(row):
            
            # Corresponding indices in full trees matrix
            i_full = i + 1
            j_full = j + 1
            
            # Look to the right, left, top, and bottom. 
            # Which trees are present in those directions?
            # Order the trees by distance. 
            
            # to the right:
            possible_trees_R = trees[i_full, j_full+1:]                      
            # to the left:
            possible_trees_L = np.flip(trees[i_full,:j_full])                     
            # to the bottom:
            possible_trees_B = trees[i_full+1:, j_full]                   
            # to the top:
            possible_trees_T = np.flip(trees[:i_full,j_full])
            
            # Count, for each direction, how many of the possible trees can actually be viewed 
            # from the current tree.            
            count_R = check_view(t, possible_trees_R)
            count_L = check_view(t, possible_trees_L)
            count_B = check_view(t, possible_trees_B)         
            count_T = check_view(t, possible_trees_T)
            
            score[i_full,j_full] = count_T*count_L*count_R*count_B
            
    top_score = np.amax(score)
    
    if part == 0:
        return total_visible, top_score
    elif part == 1:
        return total_visible
    elif part == 2:
        return top_score


if __name__ == '__main__':
    input = 'input/day_8_full.txt'
    part = 0
    print(main(input, part))
