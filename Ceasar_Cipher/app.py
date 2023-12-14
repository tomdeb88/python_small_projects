alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
continue_app=True

def cipher(message,shift_no,direction):
    word=''
    for l in message:
        index=alphabet.index(l)
        if direction=='encode':
            letter=alphabet[index + shift_no]
        elif direction=='decode':
            letter=alphabet[index - shift_no]
        word+=letter
    print(f"\n\nHere is a {direction} result: {word}\n\n")

while  continue_app:
    direction=input("Type 'encode' to encrypt or typr 'decode' to decrypt:\n ").lower()
    text=input('Type your message here:\n').lower()
    shift=int(input('Type the shift number:\n'))

    cipher(text,shift,direction)

    keep_going=input('Would you like to continue? Type "yes" or "no" ').lower()
    if keep_going=='no':
        continue_app=False



