from pathlib import Path


def solve(input_text):
    """Solve part 1 of the puzzle."""
    lines = input_text.strip().split("\n")
    matrix = [list(row) for row in input_text.split("\n")]
    beam_split_count = 0
    for row in matrix:
        print(row)

    def chevron_split(matrix, row, col):
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

    def check_S_or_pipe(matrix, row, col):
        if (row + 1) < len(matrix) - 1:
            if matrix[row + 1][col] == "^":
                matrix[row + 1][col - 1] = "|"
                matrix[row + 1][col + 1] = "|"
                return 1
            elif (
                matrix[row][col] == "S"
                or matrix[row][col] == "|"
                and matrix[row + 1][col] != "^"
            ):
                matrix[row + 1][col] = "|"
                return 0
            return 0
        return 0

        # if down direction == "^":
        #   chevron split function & add to count

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "S" or matrix[i][j] == "|":
                beam_split_count += check_S_or_pipe(matrix, i, j)
            # elif matrix[i][j] == "^":
            #     chevron_split(matrix, i, j)
            else:
                continue
    for row in matrix:
        print(row)

    return beam_split_count


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day07.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
