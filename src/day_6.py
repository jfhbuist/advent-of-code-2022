# day_6.py

def find_marker(datastream, marker_length):
    for idx, c in enumerate(datastream):
        seq = datastream[idx:idx+marker_length]
        if len(set(seq)) == len(seq):
            # marker = seq
            marker_idx = idx+marker_length
            break
    return marker_idx


def main(input, part):

    with open(input) as f:
        datastream = f.read().rstrip('\n')
        marker_idx_1 = find_marker(datastream, 4)
        marker_idx_2 = find_marker(datastream, 14)

    if part == 0:
        return marker_idx_1, marker_idx_2
    elif part == 1:
        return marker_idx_1
    elif part == 2:
        return marker_idx_2


if __name__ == '__main__':
    input = 'input/day_6_full.txt'
    part = 0
    print(main(input, part))
