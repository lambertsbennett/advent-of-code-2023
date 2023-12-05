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


# I know passing the whole matrix in each time is wasteful.
def search_for_symbols(input_mat, line_num, num_pos_tuple) -> int:
    special_characters = "!@#$%^&*()-+?_=,<>/"
    pos = num_pos_tuple[1]
    print(pos)
    if line_num == 0:
        above_line = 0
    else:
        above_line = line_num - 1
    if line_num == len(input_mat) - 1:
        below_line = -1
    else:
        below_line = line_num + 1

    min_pos = max(0, pos[0] - 1)
    if pos[-1] >= len(input_mat[line_num]) - 2:
        max_pos = -1
    else:
        max_pos = pos[-1] + 2

    # print(f"length: {len(input_mat[line_num]) - 1}, pos: {pos[-1]}, max_pos: {max_pos}")
    search_space = [
        input_mat[line_num][min_pos],
        input_mat[line_num][max_pos - 1],
        input_mat[above_line][min_pos:max_pos],
        input_mat[below_line][min_pos:max_pos],
    ]
    print(search_space)

    search_str = "".join(search_space)
    if any(c in special_characters for c in search_str):
        return num_pos_tuple[0]
    else:
        return 0


results = []
with open("input.txt", "r") as f:
    input_matrix = []
    locs = []
    results = []
    for i, line in enumerate(f):
        input_matrix.append(line)
        locs.append((i, extract_numbers_positions(line)))
    for loc in locs:
        line_num = loc[0]
        for num_tup in loc[1]:
            results.append(search_for_symbols(input_matrix, line_num, num_tup))

print(sum(results))

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
# results = []
# for i, line in enumerate(test_mat):
#     locs.append((i, extract_numbers_positions(line)))
# for loc in locs:
#     line_num = loc[0]
#     for num_tup in loc[1]:
#         results.append(search_for_symbols(test_mat, line_num, num_tup))
# print(results)


# print(sum(results))
