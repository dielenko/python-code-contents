from art import logo
from script import alphabet

# Combine the encrypt and decrypt functions into a single function called caesar().
def ceaser(text_input, shift_input, direction_input):
    cipher = []
    for char in text_input:
        # Mitigate if the user enters a number/symbol/space
        if char.isalpha(): 
            char_index = alphabet.index(char)
            if direction_input == 'encode':
                calc_shift = char_index + shift_input
            elif direction_input == 'decode':
                calc_shift = char_index - shift_input
            # Mitigate index out of range error when try to encode a dedicated word for example 'zulu'.
            if calc_shift >= len(alphabet):
                calc_reverse_shift = calc_shift - len(alphabet)
                cipher.append(alphabet[calc_reverse_shift])
            else:
                cipher.append(alphabet[calc_shift])
        else:
            cipher.append(char)
        cipher_output = ''.join(cipher)
    print(f"The {direction_input}d text is {cipher_output}")

#Import and print the logo from art.py when the program starts.
print(logo)

# Creating a while loop that continues to execute the program if the user types 'yes'.
run_again = 'yes'

while run_again == 'yes':
    # Get the user inputs
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Add checkpoint with modulus (%) so that the program continues to work even if the user enters a shift number greater than 26. 
    shift = shift % 26
    ceaser(text_input=text, shift_input=shift, direction_input=direction)
    run_again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()