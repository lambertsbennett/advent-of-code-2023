words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
value_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_first_last_digit(input_str: str) -> int:
    res_map = {}
    for word in words:
        ind = 0
        while ind != -1:
            print(ind)
            ind = input_str.find(word, ind)
            if (ind != -1) and (
                ind <= # Minimum index in res_map
            ):
                res_map["first"] = {word: ind}
            elif (ind != -1) and (
                ind > # Maximum index in res_map
            ):
                res_map["last"] = {word, ind}
            print(res_map)
    result_arr = [
        value_map[list(res_map.get("first").keys())[0]],
        value_map[list(res_map.get("last", res_map["first"]).keys())[0]],
    ]
    print(result_arr)
    return int("".join(result_arr))


result = []

with open("input.txt", "r") as f:
    for line in f:
        result.append(get_first_last_digit(line))

print(sum(result))
