# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', 
# except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'


def string_converter(str_i):
    str_o = str_i.lower()
    
    char1 = str_o[0]

    str_o = str_o.replace(char1, '$' )

    str_o = char1 + str_o[1:]

    return str_o

print(string_converter("Folabrafif"))