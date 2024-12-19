def shift_cipher(init_str: str, shift_number: int):
    """
    This function used to shift character to an amount
    """
    # upper case of input to make characters in init string from A -> Z
    init_str = init_str.upper()
    result = ""

    # fist character number in ASCII
    first_character_number = ord("A")
    # from A -> Z we have 26 characters
    number_of_character = 26

    for character in init_str:
        # for each character in init string, convert from character to number, reduce number to make it from 0 -> 26 then mod 26 to make the number in range 0 -> 26
        # after shifting adding ASCII number of 'A' then convert back to character we can get the result.
        character_to_number = ord(character)

        number_after_shifting = (
            character_to_number - first_character_number + shift_number
        ) % number_of_character + first_character_number

        result += chr(number_after_shifting)
    return result


# main function start here
# first line enter a text input
initial_data = input()
# the number want to add
shift_number = int(input())

result = shift_cipher(initial_data, shift_number)
print(result)
