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
    num_results = []
    results = []
    for i, c in enumerate(input_str):
        if c.isnumeric():
            num_results.append((c, i))
    for word in words:
        ind = 0
        while ind != -1:
            word_loc = input_str.find(word, ind)
            if word_loc != -1:
                results.append((value_map[word], word_loc))
                ind = word_loc + len(word) - 1
            else:
                ind = -1
    results.extend(num_results)
    results.sort(key=lambda item: item[1])
    return int("".join([results[0][0], results[-1][0]]))


result = []

with open("input.txt", "r") as f:
    i = 0
    for line in f:
        result.append(get_first_last_digit(line))
print(sum(result))
