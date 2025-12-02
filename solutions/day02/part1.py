from pathlib import Path

def solve(input_text):
    """Solve part 1 of the puzzle."""
    id_ranges = input_text.strip().split(',')
    invalid_id_sum = 0


    def generate_ids_from_range(id_range):
        generated_range = []
        start, end = map(int, id_range.split('-'))
        difference= end - start
        for i in range(difference + 1):
            generated_range.append(start + i)
        
        return generated_range


    def check_id_range(id_range):
        invalid_id_sum = 0
        
        for id in id_range:
            if str(id)[0] == "0":
                print(f"Caught a leading zero id! {id}")
                continue
            invalid_id = check_id(str(id))
            invalid_id_sum += int(invalid_id)
        return invalid_id_sum


    def check_id(id):
        # Check for repeating pattern exactly twice
        res = len(id) % 2 == 0 and id[:len(id)//2] == id[len(id)//2:]
        if res:
            return id
        return 0
 

    for id_range in id_ranges:
        generated_ids_in_range = generate_ids_from_range(id_range)
        invalid_id_sum += check_id_range(generated_ids_in_range)
    
    return invalid_id_sum

if __name__ == "__main__":
    input_file = Path(__file__).parent.parent.parent / "inputs" / "day02.txt"
    input_text = input_file.read_text()
    
    result = solve(input_text)
    print(f"Answer: {result}")
