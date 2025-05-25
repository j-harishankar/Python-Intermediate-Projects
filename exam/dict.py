word = input("Enter the string:")
d = int(input("Enter the distance"))
new = ""
for ch in word:
    count = ord(ch)
    cipher_value = count+d
    if cipher_value<=ord('z'):
        new=new+chr(cipher_value)
    else:
        cipher_value = (rd('z')-d)-(ord('a')-count-1)

