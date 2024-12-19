def vigenere_cipher(plain_text: str, keys: str):
    """
    This function used to encrypt plain text using Vigenere cipher algorithm
    """
    # first step is upper case inputs, make all character in input from A -> Z
    plain_text = plain_text.upper()
    keys = keys.upper()
    # index_keys used to loop character in keys
    index_key = 0
    # ascii_number_a is ascii number of "A", used to convert ascii number of characters in plain text in range from 0 to 25
    ascii_number_a = ord("A")
    result = ""

    for character in plain_text:
        # index_character, index_selected_key is the index of character, selected key in range from 0 to 25
        index_character = ord(character) - ascii_number_a
        index_selected_key = ord(keys[index_key]) - ascii_number_a
        # Encrypted character equal addition of index_character and index_selected_key, then mod 26 to make it in range from 0 to 25
        # Adding ascii_number_a to convert it back to character
        encrypted_character = chr(
            (index_character + index_selected_key) % 26 + ascii_number_a
        )
        # Loop index_key from 0 (first index) to last character index in keys
        # If index_key is last character index in keys, set index_key = 0 to start the loop again
        if index_key < len(keys) - 1:
            index_key += 1
        else:
            index_key = 0

        result += encrypted_character
    return result


# main function starts here
# first line is the message need to encrypt
initial_input = input()
# second input is the message used as a keys
keys = input()

result = vigenere_cipher(initial_input, keys)

print(result)
