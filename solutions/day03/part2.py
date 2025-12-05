from pathlib import Path


def solve(input_text):
    """Solve part 2 of the puzzle."""
    lines = input_text.strip().split("\n")
    sum = 0


    def process_line(line, number_of_batteries) -> int:
        battery_rack_length = len(line)

        # Using a version of a greedy algorithm
        result = []
        start = 0

        for position in range(number_of_batteries):
            remaining_batteries_needed = number_of_batteries - position - 1

            # Determines how much further we can search for the next max digit in the line/rack
            search_end = battery_rack_length - remaining_batteries_needed

            # Find the max digit in the allowed range
            max_digit = max(line[start:search_end])
            # Where that max digit is in the line/rack
            max_index = line.index(max_digit, start)
            # Gradually build the result
            result.append(max_digit)
            # Update where the next search should begin so we don't reuse digits/indexes
            start = max_index + 1

        return int("".join(result))

    for line in lines:
        jolts = process_line(line, number_of_batteries=12)
        sum += int(jolts)

    return sum


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day03.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
