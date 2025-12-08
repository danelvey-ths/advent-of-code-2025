from pathlib import Path
import datetime


def solve(input_text):
    """Solve part 1 of the puzzle."""
    lines = input_text.strip().split("\n")
    split_index = lines.index("")
    ranges = lines[:split_index]
    fresh_ids = set()
    start_time = datetime.datetime.now()

    for id_range in ranges:
        start, end = map(int, id_range.split("-"))
        for single_id in range(start, end + 1):
            fresh_ids.add(single_id)

    end_time = datetime.datetime.now()
    print(f"Time taken: {end_time - start_time}")
    # print("fresh_IDs:", fresh_ids)
    return len(fresh_ids)


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day05.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
