from typing import List


def extract_numbers_positions(line: str) -> List[tuple[int, List[int]]]:
    prev_ind = 0
    num_strs = []
    pos = []
    line_result = []
    for i, c in enumerate(line):
        if c.isnumeric() and (i - prev_ind < 2):
            num_strs.append(c)
            pos.append(i)
            prev_ind = i
            if i == len(line) - 1:
                line_result.append((int("".join(num_strs)), pos))
        else:
            if num_strs and pos:
                line_result.append((int("".join(num_strs)), pos))
            prev_ind = i
            num_strs = []
            pos = []
    return line_result


def search_for_connections(asterisk_map, line_num, num_pos_tuple, max_len) -> int:
    results = []
    pos = num_pos_tuple[1]
    if line_num == 0:
        above_line = 0
    else:
        above_line = line_num - 1
    if line_num == max_len:
        below_line = max_len
    else:
        below_line = line_num + 1

    min_pos = max(0, pos[0] - 1)
    if pos[-1] >= max_len - 1:
        max_pos = max_len
    else:
        max_pos = pos[-1] + 1

    search_space = [
        [(line_num, min_pos)],
        [(line_num, max_pos)],
        [
            (above_line, p)
            for p in range(min_pos, max_pos + 1)
            if above_line != line_num
        ],
        [
            (below_line, p)
            for p in range(min_pos, max_pos + 1)
            if below_line != line_num
        ],
    ]
    flat_search_space = []
    for loc in search_space:
        flat_search_space.extend(loc)

    for loc in flat_search_space:
        if asterisk_map.get(loc, 0) != 0:
            results.append((loc, num_pos_tuple[0]))
    return results


with open("input.txt", "r") as f:
    locs = []
    results = {}
    asterisk_map = {}

    # Ugly O(N^2)
    for i, line in enumerate(f):
        max_len = len(line) - 1
        locs.append((i, extract_numbers_positions(line)))
        for j, c in enumerate(line):
            if c == "*":
                asterisk_map[(i, j)] = 1
    for loc in locs:
        line_num = loc[0]
        for num_tup in loc[1]:
            output = search_for_connections(asterisk_map, line_num, num_tup, max_len)
            if output:
                for o in output:
                    results.setdefault(o[0], []).append(o[1])

gear_sum = 0
for val_array in list(results.values()):
    if len(val_array) == 2:
        product = val_array[0] * val_array[1]
        gear_sum = gear_sum + product

print(gear_sum)
