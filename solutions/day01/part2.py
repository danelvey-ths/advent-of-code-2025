from pathlib import Path

def move_dial(old_position, line):
    direction = line[0]
    steps = int(line[1:])
    bonus_zero_steps = 0

    if direction == "R":
        new_position = (old_position + steps) % 100
        bonus_zero_steps = (old_position + steps) // 100
        # print(f"Calculating bonus zeros going R: {old_position} + {steps} // 100 = {bonus_zero_steps} - landed on {new_position}")
    else:
        new_position = (old_position - steps) % 100
        bonus_zero_steps = ((old_position - steps) // 100) * -1
        # print(f"Calculating bonus zeros going L: {old_position} - {steps} // 100 = {bonus_zero_steps} - landed on {new_position}")

    if new_position == 0:
        bonus_zero_steps -= 1

    return new_position, bonus_zero_steps

def solve(input_text):
    """Solve part 2 of the puzzle."""

    lines = input_text.strip().split('\n')
    position = 50
    zero_count = 0

    for line in lines:
        position, bonus_zero_steps = move_dial(position, line)
        zero_count += bonus_zero_steps
        if position == 0:
            zero_count += 1
        
    return zero_count

if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day01.txt"
    input_text = input_file.read_text()
    
    result = solve(input_text)
    print(f"Answer: {result}")
