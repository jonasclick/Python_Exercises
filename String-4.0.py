# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', 
# except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'


def string_converter(string):
    input_string = string.lower()
    
    first_char = input_string[0]

    new_string = ''

    for i in input_string:
        if i == first_char:
            new_string += '$'
        else:
            new_string += i

    new_string_list = list(new_string)

    new_string_list[0] = first_char

    last_string = ''.join(new_string_list)

    return last_string

print(string_converter("Folabrafif"))