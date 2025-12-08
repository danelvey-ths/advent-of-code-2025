from pathlib import Path


def solve(input_text):
    """Solve part 1 of the puzzle."""
    lines = input_text.strip().split("\n")
    split_index = lines.index("")
    ranges = lines[:split_index]
    ids_to_check = lines[split_index + 1 :]
    set_of_ids = set()
    fresh_ids = []

    def generate_ids_from_range(id_range):
        start, end = map(int, id_range.split("-"))
        difference = end - start
        for i in range(difference + 1):
            set_of_ids.add(start + i)

    for id_range in ranges:
        generate_ids_from_range(id_range)

    for veg_id in ids_to_check:
        if int(veg_id) in set_of_ids:
            fresh_ids.append(veg_id)

    # print("Generated IDs:", set_of_ids)
    # print("IDs:", ids_to_check)
    return len(fresh_ids)


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day05.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
