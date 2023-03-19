import string
import random

def generate_key():
    # Generate random key
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    key = ''.join(alphabet)
    return key

def polyalphabetic_encrypt(plaintext, key):
    # Encrypt plaintext using polyalphabetic substitution cipher
    ciphertext = ''
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            # Shift character by corresponding amount in key
            shift = ord(key[key_index % len(key)]) - ord('a')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def polyalphabetic_decrypt(ciphertext, key):
    # Decrypt ciphertext using polyalphabetic substitution cipher
    plaintext = ''
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            # Shift character by corresponding amount in key
            shift = ord(key[key_index % len(key)]) - ord('a')
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            key_index += 1
        else:
            plaintext += char
    return plaintext

# Example usage
plaintext = "pesan anda telah dienkripsi secara end to end."
key = generate_key()
ciphertext = polyalphabetic_encrypt(plaintext, key)
decrypted_plaintext = polyalphabetic_decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Key:", key)
print("Ciphertext:", ciphertext)
print("Decrypted plaintext:", decrypted_plaintext)
