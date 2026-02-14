def encrypt(text, shift):
    result = ""

    for char in text:
        # Check if the character is a letter
        if char.isalpha():

            # Check if the letter is uppercase
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            # Convert letter to number, apply shift, and convert back
            new_char = ord(char) - base
            new_char = new_char + shift
            new_char = new_char % 26
            new_char = new_char + base

            result = result + chr(new_char)

        else:
            result += char

    return result


def secure_decrypt(encrypted_text, correct_shift):
    attempts = 3

    while attempts > 0:
        user_shift = int(input("Enter shift key to decrypt: "))

        if user_shift == correct_shift:
            print("Access granted")
            print("Decrypted text:", encrypt(encrypted_text, -user_shift))
            return
        else:
            attempts -= 1
            print("Wrong key , Attempts left:", attempts)

    print("Too many wrong attempts. Access blocked")


text = input("Enter message to encrypt: ")
shift = int(input("Set secret shift key: "))

encrypted_text = encrypt(text, shift)
print("Encrypted text:", encrypted_text)

secure_decrypt(encrypted_text, shift)
