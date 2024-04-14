# Write a Python program to calculate the length of a string.

def string_length(string):
    length = 0

    for i in string:
        length += 1

    return length


print(
    string_length("Hello, World!")
)