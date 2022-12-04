# day_4.py

input = 'input/day_4_full.txt'

contained_assignments = 0
overlapping_assignments = 0
expanded_assignments = [[], []]

with open(input) as f:
    for line in f:
        assignments = line.strip().split(',')
        for idx, assignment in enumerate(assignments):
            end_points = assignment.split('-')
            sections = list(range(int(end_points[0]), int(end_points[1])+1))
            expanded_assignments[idx] = sections
        # check if either set is a subset of the other:
        if (set(expanded_assignments[0]).issubset(expanded_assignments[1])
                or set(expanded_assignments[1]).issubset(expanded_assignments[0])):
            contained_assignments += 1
        # check if there is any overlap:
        if not set(expanded_assignments[0]).isdisjoint(expanded_assignments[1]):
            overlapping_assignments += 1


print(contained_assignments)
print(overlapping_assignments)
