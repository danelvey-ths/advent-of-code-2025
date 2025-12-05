from pathlib import Path


def solve(input_text):
    """Solve part 1 of the puzzle."""
    lines = input_text.strip().split("\n")
    sum = 0


    def process_line(line) -> int:
        max_jolt = 0

        # Try all pairs of batteries (i, j) where i < j
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                # Form a two-digit number from batteries at positions i and j
                joltage = int(line[i] + line[j])
                max_jolt = max(max_jolt, joltage)

        return max_jolt

    for line in lines:
        jolts = process_line(line)
        sum += int(jolts)

    return sum


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day03.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
