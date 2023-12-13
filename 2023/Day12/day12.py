import numpy as np

f = open("input_day.txt", "r")
data = f.read().split("\n")
f.close()

som_arrangements = 0

# i == current position within dots
# bi == current position within blocks
# current == length of current block of '#'
# state space is len(dots) * len(blocks) * len(dots)
DP = {}
def f(dots, blocks, i, bi, current):
    key = (i, bi, current)
    if key in DP:
        return DP[key]
    if i == len(dots): # at the end of the string
        if bi == len(blocks) and current == 0:
            return 1
        elif bi == len(blocks) - 1 and blocks[bi] == current:
            return 1
        else:
            return 0
    ans = 0
    for c in ['.', '#']: # 2 mogelijkheden voor vraagtegens
        if dots[i] == c or dots[i] == '?':
            if c == '.' and current == 0: 
                ans += f(dots, blocks, i+1, bi, 0) # skip leading dots
            elif c == '.' and current > 0 and bi < len(blocks) and blocks[bi] == current: # end of block
                ans += f(dots, blocks, i+1, bi+1, 0)
            elif c == '#':
                ans += f(dots, blocks, i+1, bi, current+1)
    DP[key] = ans
    return ans

for part2 in [False, True]:
    som_arrangements = 0
    for line in data:
        dots, blocks = line.split()
        if part2:
            dots = '?'.join([dots, dots, dots, dots, dots])
            blocks = ','.join([blocks, blocks, blocks, blocks, blocks])
        blocks = [int(x) for x in blocks.split(',')]
        DP.clear()
        score = f(dots, blocks, 0, 0, 0)
        som_arrangements += score
    print(som_arrangements)

# 
def get_arangements(row, groups):

    group_count = len(groups)
    permutations = dict()
    permutations[0, 0] = 1

    def is_valid(group_index, current_group_size, strict=True):
        try:
            if strict:
                return current_group_size == groups[group_index]
            else:
                return current_group_size <= groups[group_index]
        except IndexError:
            return False

    for c in row:
        new_permutations = defaultdict(int)
        for (group_index, current_group_size), count in permutations.items():
            valid = True
            if c == '#':
                current_group_size += 1
                valid = is_valid(group_index, current_group_size, False)
            elif c == '?':
                # say it's a dot
                if current_group_size > 0:
                    # check if is a valid termination (strict)
                    _valid = is_valid(group_index, current_group_size)
                    if _valid:
                        new_permutations[group_index + 1, 0] += count
                else:
                    new_permutations[group_index, current_group_size] += count
                # is a hash
                new_permutations[group_index, current_group_size + 1] += count
                continue
            else:
                if current_group_size > 0:
                    # check if is a valid termination (strict)
                    valid = is_valid(group_index, current_group_size)
                    current_group_size = 0
                    group_index += 1
            if valid:
                new_permutations[group_index, current_group_size] += count
        permutations = new_permutations

    c = 0
    for (group_index, current_group_size), count in permutations.items():
        if current_group_size > 0:
            try:
                if current_group_size != groups[group_index]:
                    continue
            except IndexError:
                continue
            group_index += 1
        if group_index == group_count:
            c += count
    return c