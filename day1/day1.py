import re
from day1Part2 import convert_to_numbers

def extract_first_and_last_numbers(text):
    # Find the first occurrence of a number in the string
    first_number = re.search(r'\d', text)
    first_number = int(first_number.group()) if first_number else 0

    # Find the last occurrence of a number in the string
    last_number = re.findall(r'\d', text)
    last_number = int(last_number[-1]) if last_number else 0

    #print(f"First occurring number: {first_number}")
    #print(f"Last occurring number: {last_number}")

    if first_number == 0:
        double_digit = 0
    elif last_number == 0:
        double_digit = first_number * 10 + first_number
    else:
        double_digit = first_number * 10 + last_number

    return double_digit


totalCalibration = 0
i = 1
# Open the file in read mode
with open('day1Input.txt', 'r') as file:
    # Read each line in the file
    for line in file: 
        input_text = line.strip()
        # Extract the first and last numbers from the string
        input_text_converted = convert_to_numbers(input_text)
        double_digit = extract_first_and_last_numbers(input_text_converted)
        print(f"original text is {input_text} and input_text_converted is : {input_text_converted} and double_digit {i} is : {double_digit}")
        i = i + 1
        totalCalibration = totalCalibration + double_digit



print(f"Sum of calibration is: {totalCalibration}")
