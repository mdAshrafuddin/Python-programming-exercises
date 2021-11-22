n = input('Please character type here ')

print("The ASCII value of {0} is ".format(ord(n)))

print('Enter a string ', end='')
text = input()
textLength = len(text)

for chr in text:
    ascci = ord(chr)
    print(chr, '\t', ascci)