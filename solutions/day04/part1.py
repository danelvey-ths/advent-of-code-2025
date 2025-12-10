from pathlib import Path


def solve(input_text):
    """Solve part 1 of the puzzle."""
    total_rolls_grabbed = 0

    matrix = [list(row) for row in input_text.split("\n")]

    # for line in matrix:
    #     print(line)

    def check_adjacents(matrix, row, col):
        length = len(matrix)
        roll_count = 0
        directions = [
            (-1, 0),  # Up
            (-1, 1),  # Up-right
            (0, 1),  # Right
            (1, 1),  # Right-down
            (1, 0),  # Down
            (1, -1),  # Down-left
            (0, -1),  # Left
            (-1, -1),  # Up-left
        ]

        if row + 1 >= len(matrix) or row - 1 < 0:
            roll_count += 0
        if col + 1 >= len(matrix[0]) or col - 1 < 0:
            roll_count += 0

        if matrix[row - 1][col] == "@":
            roll_count += 1
        if matrix[row - 1][col + 1] == "@":
            roll_count += 1
        if matrix[row][col + 1] == "@":
            roll_count += 1
        if matrix[row + 1][col + 1] == "@":
            roll_count += 1
        if matrix[row + 1][col] == "@":
            roll_count += 1
        if matrix[row + 1][col - 1] == "@":
            roll_count += 1
        if matrix[row][col - 1] == "@":
            roll_count += 1
        if matrix[row - 1][col - 1] == "@":
            roll_count += 1

        if roll_count < 4:
            print(f"Found {roll_count} as adjacents to {row}, {col}.")
            return 1
        else:
            return 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "@":
                successful_grab = check_adjacents(matrix, i, j)
                total_rolls_grabbed += successful_grab
                # break
            else:
                continue

    return total_rolls_grabbed


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day04-sample.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
