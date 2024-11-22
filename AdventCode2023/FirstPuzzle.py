file_name = "FirstPuzzleInput.txt"

# Map spelled-out numbers to their digit equivalents
spelled_digits = {
    "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
}

total = 0 #initialize total sum

def find_first_and_last_digit(line):
    words = line.split() #spliting the line into words
    first_digit = None
    last_digit = None

    #iterate through the words to find the first digit
    for word in words:
        if word.isdigit():
            first_digit = word
            break
        elif word.lower() in spelled_digits:
            first_digit = spelled_digits[word.lower()]
            break

    for word in reversed(words):
        if word.isdigit():
            last_digit = word
            break
        elif word.lower() in spelled_digits:
            last_digit =  spelled_digits[word.lower()]
            break

    return first_digit, last_digit

with open(file_name, "r") as file: #with open() ensures the file is properly closed after reading
    for line in file:
        line = line.strip() #striping white spaces
        if not line: #skip empty lines
            continue

        #Get the first and last digit:
        first_digit, last_digit = find_first_and_last_digit(line)

        if first_digit and last_digit: #both digits exist
            calibration_value = int(first_digit + last_digit)
            total += calibration_value

print("Total sum of calibration values: ", total)