from pathlib import Path

def move_dial(old_position, line):
    direction = line[0]
    steps = int(line[1:])
    zero_count = 0

    if direction == "R":
        if old_position == 0:
            zero_count = steps // 100
        else:
            zero_count = (old_position + steps) // 100
        
        new_position = (old_position + steps) % 100

    else: # direction == "L"
        if old_position == 0:
            zero_count = steps // 100
        else:
            if steps >= old_position:
                # We hit 0 at least once
                zero_count = ((steps - old_position) // 100) + 1
            else:
                zero_count = 0
        
        new_position = (old_position - steps) % 100

    return new_position, zero_count

def solve(input_text):
    """Solve part 2 of the puzzle."""

    lines = input_text.strip().split('\n')
    position = 50
    zero_count = 0

    for line in lines:
        position, line_zero_count = move_dial(position, line)
        zero_count += line_zero_count
        
    return zero_count

if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day01.txt"
    input_text = input_file.read_text()
    
    result = solve(input_text)
    print(f"Answer: {result}")



# Starting at 21, going L: 21 - 921 // 100 = 9 bonus zeros - landed on 0