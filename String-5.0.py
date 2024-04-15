# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

str_1 = 'abc'
str_2 = 'xyz'

str_1a = str_2[0:2] + str_1[2:]
str_2a = str_1[0:2] + str_2[2:]

str_3 = str_1a + ' ' + str_2a

print(str_3)