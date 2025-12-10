from pathlib import Path


def solve(input_text):
    """Solve part 1 of the puzzle."""
    lines = input_text.strip().split("\n")
    matrix = [list(row) for row in input_text.split("\n")]
    for row in matrix:
        print(row)

    def check_adjacents(matrix, row, col):
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

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "S":
                successful_grab = check_adjacents(matrix, i, j)
                # break
            elif matrix[i][j] == "|":
                successful_grab = check_adjacents(matrix, i, j)
            else:
                successful_grab = check_adjacents(matrix, i, j)

    return None


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day07-sample.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
