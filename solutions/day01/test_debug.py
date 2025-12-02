from pathlib import Path

def move_dial(old_position, line):
    direction = line[0]
    steps = int(line[1:])
    bonus_zero_steps = 0

    if direction == "R":
        new_position = (old_position + steps) % 100
        full_rotations = (old_position + steps) // 100
        if new_position == 0 and full_rotations > 0:
            bonus_zero_steps = full_rotations - 1
        else:
            bonus_zero_steps = full_rotations

    else: # direction == "L"
        new_position = (old_position - steps) % 100
        if steps > old_position:
            full_rotations = ((steps - old_position - 1) // 100) + 1
            if new_position == 0 and full_rotations > 0:
                bonus_zero_steps = full_rotations - 1
            else:
                bonus_zero_steps = full_rotations
        else:
            bonus_zero_steps = 0

    return new_position, bonus_zero_steps

def solve(input_text):
    lines = input_text.strip().split('\n')
    position = 50
    zero_count = 0

    for line in lines:
        old_pos = position
        position, bonus_zero_steps = move_dial(position, line)
        landed_on_zero = 1 if position == 0 else 0
        zero_count += bonus_zero_steps
        if position == 0:
            zero_count += 1
        print(f"{line}: {old_pos} -> {position}, bonus={bonus_zero_steps}, landed={landed_on_zero}, total={zero_count}")
        
    return zero_count

input_file = Path(__file__).parent.parent.parent / "inputs" / "day01-sample.txt"
input_text = input_file.read_text()
result = solve(input_text)
print(f"\nFinal Answer: {result}")
