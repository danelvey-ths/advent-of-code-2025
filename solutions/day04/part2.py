from pathlib import Path


def solve(input_text):
    """Solve part 1 of the puzzle."""
    total_rolls_grabbed = 0

    matrix = [list(row) for row in input_text.split("\n")]

    def check_adjacents(matrix, row, col):
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

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
                if matrix[r][c] == "@":
                    roll_count += 1

        if roll_count < 4:
            return 1
        else:
            return 0

    while True:
        rolls_to_update = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == "@":
                    successful_grab = check_adjacents(matrix, i, j)
                    if successful_grab:
                        rolls_to_update.append((i, j))
                    total_rolls_grabbed += successful_grab
                    if rolls_to_update:
                        for r, c in rolls_to_update:
                            matrix[r][c] = "X"
                else:
                    continue
        if not rolls_to_update:
            break
    return total_rolls_grabbed


if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day04.txt"
    input_text = input_file.read_text()

    result = solve(input_text)
    print(f"Answer: {result}")
