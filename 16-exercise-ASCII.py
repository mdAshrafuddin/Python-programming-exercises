# n = input('Please character type here ')

# print("The ASCII value of {0} is ".format(ord(n)))

# print('Enter a string ', end='')
# text = input()
# textLength = len(text)

print("Enter a String: ", end="")
text  = input()
textlength = len(text)

for char in text:
    ascci = ord(char)
    print(char, '\t', ascci)



