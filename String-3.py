# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
# If the string length is less than 2, return the empty string instead.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String


input_string = input("Please provide a String: ")

input_string = "w3resource"


def string_operation(input_string):
    length = 0

    for i in input_string:
        length += 1


    output_string = ""

    if length < 2:
        return output_string
    else:
        output_string += input_string[0]
        output_string += input_string[1]

        output_string += input_string[int(length)-2]
        output_string += input_string[int(length)-1]

        return output_string


print(string_operation(input_string))


###############

my_string = "Helio, World!"
print(my_string[2:6])  # Output: 'llo,'
print(my_string[:5])   # Output: 'Hello'
print(my_string[7:])   # Output: 'World!'


print(my_string[1:-1])