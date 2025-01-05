import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#Todo-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

# def encoder(text,shift):
#     encode_list = []   
#     for j in text:
#         index = 0
#         index = alphabet.index(j)+shift
#         encode_list.append(alphabet[index%len(alphabet)])
#     print(f"{''.join(encode_list)}")
# def decoder(text,shift):

#     decoding_string=""
#     for j in text:
#         index_d = 0
#         index_d += alphabet.index(j)-shift
#         decoding_string += alphabet[index_d%26]
#     print(decoding_string)
print(art.logo)
def ceaser(text,shift,direction):
    decoded_string = ""
    if direction == "decode":
        shift*=-1
    for char in text:
        if char in alphabet:
            position = alphabet.index(char)+shift
            decoded_string+=alphabet[position%len(alphabet)]
        else:
            decoded_string+=char
    print(f"The string i.e {direction}ed is {decoded_string}")
    
should_continue = True
while should_continue :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text,shift,direction)
    repeat=input("Do you want to repeat the program.\n[1]Yes\n[2]No")
    if repeat=='no':
        should_continue=False
        print('program completed')


