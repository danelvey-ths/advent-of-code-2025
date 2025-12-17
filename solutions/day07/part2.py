from pathlib import Path
from datetime import datetime


def solve(input_text):
    """Solve part 2 of the puzzle."""
    matrix = [list(row) for row in input_text.split("\n")]
    rows = len(matrix)
    cols = len(matrix[0])

    start_row, start_col = None, None
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "S":
                start_row, start_col = i, j
                break
        if start_row is not None:
            break
    start_time = datetime.now()
    memo = {}

    def explore(row, col, direction):
        """
        Recursively explore from a given position and direction.
        Returns the number of distinct timelines from this state.

        direction: "down", "left", "right"
        """
        # Create a state key for memoization
        state = (row, col, direction)
        if state in memo:
            return memo[state]

        # Base case: out of bounds means we've reached the end of a timeline
        if row >= rows or row < 0 or col >= cols or col < 0:
            return 1  # Counts as a completed timeline

        # Calculate the next position based on direction
        if direction == "down":
            next_row, next_col = row + 1, col
        elif direction == "left":
            next_row, next_col = row + 1, col - 1
        elif direction == "right":
            next_row, next_col = row + 1, col + 1
        else:
            return 0  # Invalid direction

        # check if the next position is out of bounds
        if next_row >= rows or next_col < 0 or next_col >= cols:
            return 1  # Reached the end of a timeline
        # Check if the next position has a splitter
        elif (
            next_row < rows
            and next_col >= 0
            and next_col < cols
            and matrix[next_row][next_col] == "^"
        ):
            # Hit a splitter - particle splits into left and right
            # Each branch continues downwards from the splitter position
            left_timelines = explore(next_row, next_col, "left")
            right_timelines = explore(next_row, next_col, "right")
            result = left_timelines + right_timelines
        else:
            # Continue in the same direction (always moving down one row)
            result = explore(next_row, next_col, "down")

        memo[state] = result
        return result

    total_timelines = explore(start_row, start_col, "down")
    end_time = datetime.now()
    print(f"Total execution time: {end_time - start_time}")
    return total_timelines


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day07.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
