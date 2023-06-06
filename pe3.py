

alphabet = "abcdefghijklmnopqrstuvwxyz"

input_text = input("Enter the text you want to encode: ")

shift = int(input("Please enter the shift you want to use to encode the entered text: "))

def encode(input_text, shift):
    encoded_string = ""
    for i in input_text:
        encoded_text = alphabet[alphabet.find(i) + shift - 1] 
        encoded_string += encoded_text
    return encoded_string
    print("The encoded text is: " + encoded_string)

encoded_text = encode(input_text, shift)

print(encoded_text)

def decode(encoded_string, shift):
    decoded_string = ""
    if encoded_string is False:
        encoded_string = input("Enter the text you want to decode: ")
    else:
        for i in encoded_string:
            decoded_text = alphabet[alphabet.find(i) - shift + 1]
            decoded_string += decoded_text
        return decoded_string
    print("The decoded text is: " + decoded_string)

decoded_text = decode(encoded_text, shift)

print(decoded_text)
