# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}


def character_frequency(string):
    result = {}

    lower_case_string = string.lower()

    for i in lower_case_string:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    
    print(result.keys())

    return result

print(character_frequency("Sali zäme, alles klar bi eu?"))


