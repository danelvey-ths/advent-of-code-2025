from pathlib import Path
from functools import reduce


def solve(input_text):
    """Solve part 2 of the puzzle."""
    lines = input_text.strip().split("\n")
    result = 0
    split_lines = []

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

    # This splits each number into its own list item
    for line in lines:
        split = []
        line = list(line.split(" "))
        print(line)
        for num in line:
            if num == "":  # Check for spaces, add these in between numbers too
                split.append(" ")
                continue
            if not num.isdigit():  # Puts individual digits into the list
                split.append(num)
                continue

            num = [n for n in str(num)]
            for n in num:
                split.append(n)

        split_lines.append(split)

    for i in range(len(split_lines[-1])):
        if split_lines[-1][i] == " ":
            split_lines[-1][i] = split_lines[-1][i - 1]
        if len((split_lines[-1])) < len(split_lines[0]):
            difference = len(split_lines[0]) - len(split_lines[-1])
            for _ in range(difference):
                split_lines[-1].append(
                    split_lines[-1][-1]
                )  # Extends the last element to match length with the other rows
    # for line in split_lines:
    #     print(len(line), line)

    rotated_lines = list(zip(*split_lines[::1]))

    print()
    numbers_to_sum = []
    for i in range(len(rotated_lines)):
        col = rotated_lines[i]
        print(col)
        current_operator = col[-1]
        next_operator = rotated_lines[i + 1][-1] if i + 1 < len(rotated_lines) else None

        numbers = [int(n) for n in col[:-1] if n != " "]
        numbers = "".join(str(number) for number in numbers)
        numbers_to_sum.append(int(numbers))
        if next_operator != current_operator:
            if current_operator == "+":
                print(numbers_to_sum, current_operator)
                result += sum(numbers_to_sum)
                numbers_to_sum = []
            elif current_operator == "*":
                print(numbers_to_sum, current_operator)
                result += reduce(lambda x, y: x * y, numbers_to_sum)
                numbers_to_sum = []
    return result


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day06.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
