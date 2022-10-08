from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']


def decode(text, shift):
    return encode(text, -shift)


def encode(text, shift):
    new_text = ""
    for character in text:
        if character in alphabet:
            new_index = (alphabet.index(character) + shift) % len(alphabet)
            new_text += alphabet[new_index]
        else:
            new_text += character
    return new_text


go_again = 'yes'
while go_again == 'yes':
    direction = ''
    while (direction not in ('encode', 'decode')):
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your text:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if (direction == 'encode'):
        new_text = encode(text, shift)
    elif (direction == 'decode'):
        new_text = decode(text, shift)
    print(f"Here's the {direction}d result: {new_text}")
    go_again = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
