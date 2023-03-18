# Fungsi untuk mengenkripsi pesan dengan menggunakan Shift Cipher
def shift_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Konversi karakter ke kode ASCII
            char_code = ord(char)
            # Shift karakter sebanyak key
            shifted_code = (char_code - 65 + key) % 26 + 65
            # Konversi kembali ke karakter
            shifted_char = chr(shifted_code)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

# Fungsi untuk mendekripsi pesan dengan menggunakan Shift Cipher
def shift_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Konversi karakter ke kode ASCII
            char_code = ord(char)
            # Shift karakter mundur sebanyak key
            shifted_code = (char_code - 65 - key) % 26 + 65
            # Konversi kembali ke karakter
            shifted_char = chr(shifted_code)
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext

# Contoh penggunaan Shift Cipher
plaintext = "AKU SAYANG KAMU SEBANYAK 25"
key = 25
ciphertext = shift_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_text = shift_decrypt(ciphertext, key)
print("Plaintext:", decrypted_text)

