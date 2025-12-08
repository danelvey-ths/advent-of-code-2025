from pathlib import Path


def solve(input_text):
    """Solve part 1 of the puzzle."""
    lines = input_text.strip().split("\n")
    split_index = lines.index("")
    ranges = lines[:split_index]
    fresh_ids = set()

    """
        The ranges are all we care about. I want to know the numbers in between those ranges. 
        Don't try to generate all the numbers in between because this will crash the machine.
        Just add what the difference is in the ranges and then we can add all of those numbers together to get the total count of fresh IDs.

        I need to factor in duplicates in the ranges
    """

    for id_range in ranges:  # This is a solution that generates all the ids - this will use a tonne of memory
        start, end = map(int, id_range.split("-"))
        difference = end - start
        for i in range(difference + 1):
            fresh_ids.add(start + i)

    return len(fresh_ids)


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day05-sample.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
