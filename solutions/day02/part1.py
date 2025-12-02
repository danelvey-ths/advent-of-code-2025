from pathlib import Path

def solve(input_text):
    """Solve part 1 of the puzzle."""
    id_ranges = input_text.strip().split(',')


    def generate_ids_from_range(id_range):
        generated_range = []
        start, end = map(int, id_range.split('-'))
        difference= end - start
        for i in range(difference + 1):
            generated_range.append(start + i)
        
        print(id_range, generated_range)
        return generated_range


    def check_id_range(id_range):
        if str(id_range[0]) == "0":
            pass
           
    
    for id_range in id_ranges:
        generated_ids_in_range = generate_ids_from_range(id_range)
        check_id_range(generated_ids_in_range)
    
    return None

if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day02-sample.txt"
    input_text = input_file.read_text()
    
    result = solve(input_text)
    print(f"Answer: {result}")
