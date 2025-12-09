from pathlib import Path
from functools import reduce


def solve(input_text):
    """Solve part 2 of the puzzle."""
    lines = input_text.strip().split("\n")
    stripped_lines = []
    result = 0
    split_reversed_lines = []

    """
        The last line is always the operation to be performed.
        The last line always has the operator at the start, then the amount of spaces between it and the next one is the "width" of the column
        We need to reverse the lines
        123 328  51  64 
         45 64  387  23 
          6 98  215 314
        *   +   *   +

        right to left becomes 4 + 431 + 623 = 1058
                              175 * 581 * 32 = 3253600
                              8 + 248 + 369 = 625
                              356 * 24 * 1 = 8544
                              sums to 3263827
    """
    for line in lines:
        split_reversed = []
        line = list(line.split(" "))
        print(line)
        for num in line:
            if num == "+" or num == "*" and len(split_reversed) < 1:
                split_reversed.insert(0, "")
            if not num.isdigit():
                split_reversed.append(num)
                continue

            num = [n for n in str(num)]
            num = list(reversed(num))
            for n in num:
                split_reversed.append(n)
            # print(num)

        split_reversed_lines.append(split_reversed)

    for line in split_reversed_lines:
        print(len(line), line)

    rotated_lines = list(zip(*stripped_lines[::-1]))

    # for line in rotated_lines:
    #     operator = line[0]
    #     numbers = tuple(map(int, line[1:]))

    #     if operator == "+":
    #         result += sum(numbers)
    #     elif operator == "*":
    #         result += reduce(lambda x, y: x * y, numbers)

    return result


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day06-sample.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
