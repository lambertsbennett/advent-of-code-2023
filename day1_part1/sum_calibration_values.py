def get_first_last_digit(input_str: str) -> int:
    res_map = {}
    for c in input_str:
        if c.isnumeric():
            if "first" not in res_map.keys():
                res_map["first"] = c
            else:
                res_map["last"] = c
    result_arr = [res_map.get("first"), res_map.get("last", res_map["first"])]
    print(result_arr)
    return int("".join(result_arr))


result = []

with open("input.txt", "r") as f:
    for line in f:
        result.append(get_first_last_digit(line))

print(sum(result))
