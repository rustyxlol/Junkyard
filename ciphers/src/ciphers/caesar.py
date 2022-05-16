"""
Encrypts/Decrypts text using Caesar Cipher
"""


class Caesar:
    """
    Caesar cipher is a substition cipher in which
    which each letter in the plaintext is 'shifted'
    a certain number of places down the alphabet
    More: http://practicalcryptography.com/ciphers/caesar-cipher/
    """

    def __init__(self, shift_key=1):
        self.shift_key = shift_key

    def encrypt(self, message):
        result = ''

        for letter in message:
            if letter.isalpha():
                if letter.isupper():
                    result += chr(((ord(letter) - 65 +
                                    self.shift_key) % 26) + 65)
                else:
                    result += chr(((ord(letter) - 97 +
                                    self.shift_key) % 26) + 97)
            else:
                result += letter

        return result

    def decrypt(self, message):
        result = ''
        for letter in message:
            if letter.isalpha():
                if letter.isupper():
                    result += chr(((ord(letter) - 65 -
                                    self.shift_key) % 26) + 65)
                else:
                    result += chr(((ord(letter) - 97 -
                                    self.shift_key) % 26) + 97)
            else:
                result += letter

        return result


if __name__ == "__main__":

    while True:
        print("PRESS [E] TO ENCRYPT")
        print("PRESS [D] TO DECRYPT")
        choice = input("ENTER: ")

        print()

        if choice.lower() not in ('e', 'd'):
            print("PLEASE ENTER VALID CHOICE")
            continue

        print()

        if choice.lower() == 'e':
            message = input("ENTER MESSAGE TO ENCRYPT: ")
            shift_key = int(input("ENTER SHIFT KEY: "))
            cipher = Caesar(shift_key)
            encrypted_message = cipher.encrypt(message)
            print("ENCRYPTED MESSAGE IS: ", encrypted_message)

        if choice.lower() == 'd':
            message = input("ENTER MESSAGE TO DECRYPT: ")
            shift_key = int(input("ENTER SHIFT KEY: "))
            cipher = Caesar(shift_key)
            decrypted_message = cipher.decrypt(message)
            print("DECRYPTED MESSAGE IS: ", decrypted_message)

        print()

        run_again = input("Press any key to quit, Y to run again: ")
        if run_again.lower() == 'y':
            continue
        break
