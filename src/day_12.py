# day_12.py

import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path


def parse_input(input):
    with open(input) as f:
        # initialize numpy array
        hills = np.array([[ord(h)-96 for h in list(f.readline().strip())]])
        # add each line to array
        for line in f:
            hills = np.append(hills, [[ord(h)-96 for h in list(line.strip())]], axis=0)
        # Fix array for S
        hills[hills == -13] = 0
        # Fix array for E
        hills[hills == -27] = 27

    return hills


def flatten_index(idx, shape):
    idx_flat = int(idx[0]*shape[1] + idx[1])
    return idx_flat


def get_path(Pr, i, j):
    path = [j]
    k = j
    while Pr[i, k] != -9999:
        path.append(Pr[i, k])
        k = Pr[i, k]
    return path[::-1]


def core(input, part):

    hills = parse_input(input)
    shape = np.shape(hills)
    size = np.size(hills)
    end = np.where(hills == 27)
    end_flat = flatten_index(end, shape)

    connections = np.zeros((size, size),dtype=int)

    for idx1, x1 in np.ndenumerate(hills):
        idx1_flat = flatten_index(idx1, shape)
        for idx2, x2 in np.ndenumerate(hills):
            idx2_flat = flatten_index(idx2, shape)
            if ( ((abs(idx2[0]-idx1[0]) == 1) and (abs(idx2[1]-idx1[1]) == 0)) or ((abs(idx2[1]-idx1[1]) == 1) and (abs(idx2[0]-idx1[0]) == 0)) ):
                if x2-x1 <= 1:
                    connections[idx1_flat, idx2_flat] = 1

    # graph = csr_matrix(connections)
    # dist_matrix, predecessors = shortest_path(connections, directed=True, method='FW', return_predecessors=True)
    # distance = int(dist_matrix[start_flat, end_flat])
    # path = get_path(predecessors, start_flat, end_flat)

    if part == 0:
        return connections
    elif part == 1:
        start = np.where(hills == 0)
        start_flat = flatten_index(start, shape)
        dist_matrix = shortest_path(connections, directed=True, indices=start_flat, return_predecessors=False)
        distance = int(dist_matrix[end_flat])
        return distance
    elif part == 2:
        start = np.argwhere(hills == 1)
        start_flat = []
        for idx in start:
            start_flat.append(flatten_index(idx, shape))
        dist_matrix = shortest_path(connections, directed=True, indices=start_flat, return_predecessors=False)
        distances = []
        for idx, row in enumerate(dist_matrix):
            distances.append(row[end_flat])
        distance = int(min(distances))
        return distance


def main(input, part):
    if part == 0:
        output_1 = core(input, 1)
        output_2 = core(input, 2)
        return output_1, output_2
    else:
        output = core(input, part)
        return output

if __name__ == '__main__':
    # input = 'input_test/day_12.txt'
    input = 'input_full/day_12.txt'
    part = 0
    print(main(input, part))
