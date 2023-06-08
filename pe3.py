alphabet = "abcdefghijklmnopqrstuvwxyz"
input_text = input("Enter the text you want to encode: ")
shift = int(input("Please enter the shift you want to use to encode the entered text: "))

def encode(input_text, shift):
    encoded_string = ""
    for char in input_text:
        if char in alphabet:
            encoded_index = (alphabet.find(char) + shift - 1) % 26
            encoded_char = alphabet[encoded_index]
            encoded_string += encoded_char
        else:
            encoded_string += char
    return encoded_string

def decode(encoded_string, shift):
    decoded_string = ""
    for char in encoded_string:
        if char in alphabet:
            decoded_index = (alphabet.find(char) - shift + 1) % 26
            decoded_char = alphabet[decoded_index]
            decoded_string += decoded_char
        else:
            decoded_string += char
    return decoded_string

encoded_text = encode(input_text, shift)

print("The encoded text is:", encoded_text)

decoded_text = decode(encoded_text, shift)

print("The decoded text is:", decoded_text)


