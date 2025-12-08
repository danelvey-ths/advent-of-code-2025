from pathlib import Path
import datetime


def solve(input_text):
    """Solve part 1 of the puzzle."""
    lines = input_text.strip().split("\n")
    split_index = lines.index("")
    ranges = lines[:split_index]
    ranges.sort(key=lambda x: int(x.split("-")[0]))  # Sort ranges by their start value
    number_of_fresh_ids = 0
    start_time = datetime.datetime.now()

    def merge_intervals(intervals):
        merged_intervals = []

        merged_intervals = [intervals[0]]

        for current in intervals:
            last_merged = merged_intervals[-1]

            # If the current interval overlaps with the last merged interval, merge them
            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # Otherwise, add the current interval to the merged list
                merged_intervals.append(current)

        return merged_intervals

    merged_ranges = merge_intervals([list(map(int, r.split("-"))) for r in ranges])

    for id_range in merged_ranges:
        start, end = id_range
        difference = end - start + 1
        number_of_fresh_ids += difference

    end_time = datetime.datetime.now()
    print(f"Time taken: {end_time - start_time}")
    # print("fresh_IDs:", fresh_ids)
    return number_of_fresh_ids


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day05.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
