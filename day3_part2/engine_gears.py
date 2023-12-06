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
        max_pos = pos[-1] + 2

    search_space = [
        (line_num, min_pos),
        (line_num, max_pos - 1),
        [(above_line, p) for p in range(min_pos, max_pos)],
        [(below_line, p) for p in range(min_pos, max_pos)],
    ]
    flat_search_space = []
    for loc in search_space:
        flat_search_space.extend(loc)

    for loc in flat_search_space:
        if asterisk_map.get(loc, 0) != 0:
            results.append((loc, num_pos_tuple[0]))
    return results


# with open("input.txt", "r") as f:
#     locs = []
#     results = {}
#     asterisk_map = {}

#     # Ugly O(N^2)
#     for i, line in enumerate(f):
#         max_len = len(line) - 1
#         locs.append((i, extract_numbers_positions(line)))
#         for j, c in enumerate(line):
#             if c == "*":
#                 asterisk_map[(i, j)] = 1
#     for loc in locs:
#         line_num = loc[0]
#         for num_tup in loc[1]:
#             output = search_for_connections(asterisk_map, line_num, num_tup, max_len)
#             if output:
#                 for o in output:
#                     results.setdefault(o[0], []).append(o[1])


# gear_sum = 0
# for val_array in list(results.values()):
#     print(val_array)
#     if len(val_array) == 2:
#         product = val_array[0] * val_array[1]
#     gear_sum = gear_sum + product

# print(gear_sum)

# test_mat = [
#     "467..114..",
#     "...*......",
#     "..35..633.",
#     "......#...",
#     "617*......",
#     ".....+.58.",
#     "..592.....",
#     "......755.",
#     "...$.*....",
#     ".664.598..",
# ]
# locs = []
# results = {}
# asterisk_map = {}
# max_len = len(test_mat[0]) - 1
# for i, line in enumerate(test_mat):
#     locs.append((i, extract_numbers_positions(line)))
#     for j, c in enumerate(line):
#         if c == "*":
#             asterisk_map[(i, j)] = 1
# for loc in locs:
#     line_num = loc[0]
#     for num_tup in loc[1]:
#         output = search_for_connections(asterisk_map, line_num, num_tup, max_len)
#         if output:
#             for o in output:
#                 results.setdefault(o[0], []).append(o[1])

# print(results)
# gear_sum = 0
# for val_array in list(results.values()):
#     if len(val_array) == 2:
#         product = val_array[0] * val_array[1]
#     gear_sum = gear_sum + product

# print(gear_sum)

test_input = [
    "........954......104.......52......70..............206.806........708..........................217...............................440........",
    ".......@...................*.............................*.664..............677................@....459.........687.........................",
    "..................378.....398........548..495..........983....*................*..282.................*...........$.248.....409.......165...",
    "......261........................704.&.......*................943...615.504.....6....*773..........687..../973.2*.....=.311*....*..../......",
]
locs = []
results = {}
asterisk_map = {}
max_len = len(test_input[0]) - 1
for i, line in enumerate(test_input):
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

print(results)
print(gear_sum)

assert gear_sum == (
    52 * 398
    + 806 * 983
    + 664 * 943
    + 677 * 6
    + 459 * 687
    + 282 * 773
    + 459 * 687
    + 311 * 409
)
