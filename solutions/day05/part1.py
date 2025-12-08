from pathlib import Path


def solve(input_text):
    """Solve part 1 of the puzzle."""
    lines = input_text.strip().split("\n")
    split_index = lines.index("")
    ranges = lines[:split_index]
    ids_to_check = lines[split_index + 1 :]
    fresh_ids = set()

    for id_range in ranges:
        start, end = map(int, id_range.split("-"))
        for veg_id in ids_to_check:
            veg_id_int = int(veg_id)
            if veg_id_int >= start and veg_id_int <= end:
                fresh_ids.add(veg_id_int)

    return len(fresh_ids)


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day05.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
