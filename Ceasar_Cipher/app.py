alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction=input("Type 'encode' to encrypt or typr 'decode' to decrypt:\n ").lower()
text=input('Type your message here:\n').lower()
shift=int(input('Type the shift number:\n'))

word=None 

if direction=='encode':

    def encrypt(message,shift):
        encrypted=''
        for l in message:
            index=alphabet.index(l)
            letter=alphabet[index+shift]
            encrypted+=letter
        return encrypted
    word=encrypt(text,shift)
    print(word)



elif direction=='decode':
    def decrypt(text_decrypted,shift):

        for l in text_decrypted:
            decrypted=''
            index=alphabet.index(l)
            letter=alphabet[index-shift]
            decrypted+=letter
            return decrypted

    decrypted_word=decrypt(word,shift)
    print(decrypted_word)




