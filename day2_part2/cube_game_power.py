from typing import List


def get_line_values_id(line: str) -> (List[str], int):
    return (line.split(":")[1], int(line.split(":")[0].replace("Game ", "")))


def get_values(sub_line: List[str]) -> dict[str, int]:
    pairs = sub_line.split(",")
    value_map = {"red": 0, "green": 0, "blue": 0}
    for p in pairs:
        r = p.strip().split(" ")
        val = int(r[0])
        key = r[1]
        if val > value_map[key]:
            value_map[key] = val
    return value_map


def get_power(value_map: dict[str, int]) -> int:
    power = 1
    for val in list(value_map.values()):
        power = power * val
    return power


def compute_power(line: str) -> int:
    values, _ = get_line_values_id(line)
    line_map = {"red": 0, "green": 0, "blue": 0}
    sublines = values.split(";")
    for s in sublines:
        s_map = get_values(s)
        for key in s_map.keys():
            if s_map[key] > line_map[key]:
                line_map[key] = s_map[key]
    power = get_power(line_map)
    return power


results = []
with open("input.txt", "r") as f:
    for line in f:
        results.append(compute_power(line))

print(sum(results))
