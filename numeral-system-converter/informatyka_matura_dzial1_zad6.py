def convert_to_decimal(number):
    decimal_value = 0
    number = [int(char) for char in str(number)]
    for i in range(len(number)):
        if number[-i - 1] == 1: decimal_value += 2 ** i
    return decimal_value

with open("dane") as r:
    numbers = r.read().splitlines()

decimal_numbers = [0]*len(numbers)
for i in range(len(numbers)):
    decimal_numbers[i] = convert_to_decimal(numbers[i])

def divisible_by_eight():
    number_of_divisible_by_eight = 0
    for i in range(len(decimal_numbers)):
        if ((decimal_numbers[i])%8==0): number_of_divisible_by_eight  +=  1
    return  number_of_divisible_by_eight

def highest_number():
    highest_number_index = 0
    for i in range(len(decimal_numbers)):
        if decimal_numbers[i] > decimal_numbers[highest_number_index]: highest_number_index = i
    print(f"wynik: {decimal_numbers[highest_number_index]}, wiersz: {highest_number_index}")



highest_number()