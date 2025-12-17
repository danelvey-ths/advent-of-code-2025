from pathlib import Path


def solve(input_text):
    """Solve part 1 of the puzzle."""
    matrix = [list(row) for row in input_text.split("\n")]
    beam_split_count = 0

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

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "S" or matrix[i][j] == "|":
                beam_split_count += check_S_or_pipe(matrix, i, j)
            else:
                continue

    return beam_split_count


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day07.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
