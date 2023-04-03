# read the encrypted file
with open('cexercise1.txt', 'r') as f:
    encrypted = f.read()

# read the text file containing the String
with open('tess26.txt', 'r') as f:
    text = f.read()

# decrypt the Caesar Cipher
def caesar_decrypt(text, shift):
    decrypted = ''
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - shift - 65) % 26 + 65)
            decrypted += shifted_char
        else:
            decrypted += char
    return decrypted

# loop over all possible shifts and compare to the decrypted string to what's in tess26
for shift in range(26):
    decrypted = caesar_decrypt(encrypted, shift)
    if all(word in text for word in decrypted.split()):
        print("The decrypted string is:", decrypted, " Which also appears in tess26")
        break
else:
    print("No matching string found.")
