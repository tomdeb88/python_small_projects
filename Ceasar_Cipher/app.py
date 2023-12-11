alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=input("Type 'encode' to encrypt or typr 'decode' to decrypt:\n ")
text=input('Type your message here:\n').lower()
shift=int(input('Type the shift number:\n'))



def encrypt(message,shift):
    encrypted=''
    for l in text:
        index=alphabet.index(l)
        letter=alphabet[index+shift]
        encrypted+=letter
    print(encrypted)

encrypt(text,shift)
    