from typing import List

value_map = {"red": 12, "green": 13, "blue": 14}


def get_line_values_id(line: str) -> (List[str], int):
    return (line.split(":")[1], int(line.split(":")[0].replace("Game ", "")))


def check_plaus(sub_line: List[str]) -> bool:
    pairs = sub_line.split(",")
    for p in pairs:
        r = p.strip().split(" ")
        val = int(r[0])
        key = r[1]
        if val > value_map[key]:
            return False
    return True


def check_game_plausability(line: str) -> int:
    values, id = get_line_values_id(line)
    sublines = values.split(";")
    subline_res = []
    for s in sublines:
        subline_res.append(check_plaus(s))
    if all(subline_res):
        return id
    else:
        return 0


results = []
with open("input.txt", "r") as f:
    for line in f:
        results.append(check_game_plausability(line))

print(sum(results))
