
import random
import string

def main():
    print("This program will encrypt your text using caesar cipher, only lowercase letters!!!")
    text = input("Write text to encrypt: ")
    generate_cipher_options(text)

def generate_cipher_options(text):
    rotation = random.choice(["left","right"])
    shift_number = random.randint(1,25)
    # encrypt(text,rotation,shift_number)
    encrypt(text,"right",2)

def encrypt(text,rotation,shift_number):
    encrypted_text = ""
    for i in range(len(text)):
        digit = text[i]
        encrypted_digit = ""

        if digit in string.punctuation or digit in string.whitespace or digit in string.octdigits:
            continue
        elif rotation == "right":
            if digit.islower():
                new_index = (string.ascii_lowercase.index(digit) + shift_number) % 26
                encrypted_digit = string.ascii_lowercase[new_index]
            elif digit.isupper():
                    new_index = (string.ascii_uppercase.index(digit) + shift_number) % 26
                    encrypted_digit = string.ascii_uppercase[new_index]
        elif rotation == "left":
            if digit.islower():
                new_index = (string.ascii_lowercase.index(digit) - shift_number) % 26
                encrypted_digit = string.ascii_lowercase[new_index]
            elif digit.isupper():
                new_index = (string.ascii_uppercase.index(digit) - shift_number) % 26
                encrypted_digit = string.ascii_uppercase[new_index]

        encrypted_text += encrypted_digit
    print(f"Encryptet text: {text} is {encrypted_text}")

main()
