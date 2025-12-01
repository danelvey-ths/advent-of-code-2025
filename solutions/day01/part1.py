from pathlib import Path

def move_dial(old_position, line):
    direction = line[0]
    steps = int(line[1:])
    
    if direction == "R":
        new_position = (old_position + steps) % 100
    else: 
        new_position = (old_position - steps) % 100

    return new_position

def solve(input_text):
    """Solve part 1 of the puzzle."""

    lines = input_text.strip().split('\n')
    position = 50
    zero_count = 0

    for line in lines:
        position = move_dial(position, line)
        if position == 0:
            zero_count += 1
        
    return zero_count

if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day01.txt"
    input_text = input_file.read_text()
    
    result = solve(input_text)
    print(f"Answer: {result}")
