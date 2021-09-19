import string

# get all ascii lowercase letters
alphabets = string.ascii_lowercase
latin_alphabet = []
key_alphabet = []
encrypted_text = []

operation_text = list(input("Enter your text: \n").lower())

for char in alphabets:
    latin_alphabet.append(char)

while True:
    keyword = input("Enter a keyword: ")
    if keyword.isalpha():
        try:
            keyword.encode(encoding = 'utf-8').decode('ascii')
            break
        except UnicodeDecodeError:
            print('Failed to decode string to utf-8. Try again.')
    else:
        print("Wrong input:number Detected.Try again.")

for char in keyword:
    key_alphabet.append(char)

for i in latin_alphabet:
    if not (i in key_alphabet):
        key_alphabet.append(i)

endProgram = False
user_choice = input(
    "Enter 'encrypt' or '1' to encrypt, 'decrypt' or '2' to decrypt, 'exit' or 'q' or '0' to exit \n"
).lower()

while not endProgram:
    # search through the text

    if user_choice == 'encrypt' or user_choice == '1':
        for i in range(len(operation_text)):
            # Get the position of every character within the sentence
            if operation_text[i] == ' ':
                operation_text[i] == ' '
            else:
                temp_var = latin_alphabet.index(operation_text[i])
                encode_letter = key_alphabet[temp_var]
                encrypted_text.append(encode_letter)
        # convert the list back to a string
        print(''.join(map(str, encrypted_text)))
        endProgram = True
    
    elif user_choice == 'decrypt' or user_choice == '2':
        for i in range(len(operation_text)):
            if operation_text[i] == ' ':
                operation_text[i] == ' '
            else:
                temp_var = key_alphabet.index(operation_text[i])
                decode_letter = latin_alphabet[temp_var]
                encrypted_text.append(decode_letter)
        # convert the list back to a string
        print(''.join(map(str, encrypted_text)))
        endProgram = True

    elif user_choice == 'exit' or user_choice == 'q' or user_choice == '0':
        endProgram = True

    else:
        decide = input(
            "Invalid entry. Try again 'Y' for yes, 'N' for no: \n".lower()            
        )
        if decide == 'y' or decide == 'yes':
            operation_text = list(input("Enter your text: \n").lower())
            user_choice = input(
                "Enter 'encrypt' or '1' to encrypt, 'decrypt' or '2' to decrypt, 'exit' or 'q' or '0' to exit \n"
            ).lower()
            keyword = input("Enter a keyword: ")
        else:
            endProgram = True

# print(latin_alphabet)
# print(key_alphabet)
