from pathlib import Path
from functools import reduce


def solve(input_text):
    """Solve part 1 of the puzzle."""
    lines = input_text.strip().split("\n")
    stripped_lines = []
    result = 0

    for line in lines:
        line = line.split(" ")
        line = [x for x in line if x.strip()]
        stripped_lines.append(line)

    rotated_lines = list(zip(*stripped_lines[::-1]))

    for line in rotated_lines:
        operator = line[0]
        numbers = tuple(map(int, line[1:]))

        if operator == "+":
            result += sum(numbers)
        elif operator == "*":
            result += reduce(lambda x, y: x * y, numbers)

    return result


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day06.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
