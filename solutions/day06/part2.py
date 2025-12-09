from pathlib import Path
from functools import reduce


def solve(input_text):
    """Solve part 2 of the puzzle."""
    lines = input_text.strip().split("\n")
    result = 0
    split_lines = []

    # Splits each number into its own list item
    for line in lines:
        split = []
        line = list(line.split(" "))

        for num in line:
            if num == "":  # Check for spaces, add these in between numbers too
                split.append(" ")
                continue
            if not num.isdigit():  # Puts individual digits into the list
                split.append(num)
                continue

            # Breaks down multi-digit numbers into individual digits
            num = [n for n in str(num)]
            for n in num:
                split.append(n)

        split_lines.append(split)

    for i in range(len(split_lines[-1])):
        if len((split_lines[-1])) < len(split_lines[0]):
            difference = len(split_lines[0]) - len(split_lines[-1])
            for _ in range(difference):
                # Extends the last element to match length with the other rows
                split_lines[-1].append(" ")

    # Rotates the rows into columns so they can be processed. This also puts the operator first in each column so it's easier to predict when to perform operations
    rotated_lines = list(zip(*split_lines[::1]))

    numbers_to_sum = []
    current_operator = " "

    for i in range(len(rotated_lines)):
        col = rotated_lines[i]
        if col[-1] == " ":
            pass
        else:
            current_operator = col[-1]

        # Strip the numbers from the column list and reform them back into numbers to be calculated
        numbers = [int(n) for n in col[:-1] if n != " "]
        numbers = "".join(str(number) for number in numbers)
        numbers_to_sum.append(int(numbers))
        # Gather these numbers and perform the operation one ahead of the next operator change

        # Check if next column is an operator change or end of list
        if i + 1 < len(rotated_lines) and (
            rotated_lines[i + 1][-1] == "+" or rotated_lines[i + 1][-1] == "*"
        ):
            if current_operator == "+":
                line_operation = sum(numbers_to_sum)
                result += line_operation
                numbers_to_sum = []
                continue
            elif current_operator == "*":
                line_operation = reduce(lambda x, y: x * y, numbers_to_sum)
                result += line_operation
                numbers_to_sum = []
                continue
    # Final operation after the loop ends
    if numbers_to_sum:
        if current_operator == "+":
            line_operation = sum(numbers_to_sum)
            result += line_operation
        elif current_operator == "*":
            line_operation = reduce(lambda x, y: x * y, numbers_to_sum)
            result += line_operation

    return result


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day06.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
