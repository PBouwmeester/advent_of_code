with open("input.txt", 'r') as file:
    content = file.read().splitlines()
    

def find_first_digit(line: str, digit_dict: dict[str: str] = digit_dict) -> int:
    lowest_index = len(line)
    for i, digit_string in digit_dict.items():
        index = line.find(i)
        if (index <= lowest_index) & (index >= 0):
            lowest_index = index
            first_digit = int(i)
        
        # this 
        index = line.find(digit_string)
        if (index <= lowest_index) & (index >= 0):
            lowest_index = index
            first_digit = int(i)
    return first_digit

def calibration_values(line: str) -> int:
    return 10*find_first_digit(line) + find_first_digit(line[::-1], digit_dict=reverse_digit_dict)


def main():
    
    digit_dict = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }

    reverse_digit_dict = {key: item[::-1] for key, item in digit_dict.items()}
    
    print(f"Calibration value = {sum(calibration_values(line) for line in content)}")
    
    
if __name__ == '__main__':
    main()
    




    