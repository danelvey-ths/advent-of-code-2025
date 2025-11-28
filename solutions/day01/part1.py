from pathlib import Path

def solve(input_text):
    """Solve part 1 of the puzzle."""
    lines = input_text.strip().split('\n')
    
    # TODO: Implement solution
    
    return None

if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day01.txt"
    input_text = input_file.read_text()
    
    result = solve(input_text)
    print(f"Answer: {result}")
