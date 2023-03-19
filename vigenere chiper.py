# Fungsi untuk mengenkripsi pesan dengan menggunakan Vigenere Cipher
def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_length = len(key)
    # Konversi karakter kunci menjadi nilai numerik (A = 0, B = 1, dst.)
    key_num = [ord(k.upper()) - 65 for k in key]
    # Enkripsi setiap karakter pada plaintext dengan menggunakan nilai numerik kunci yang sesuai
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            # Konversi karakter pesan menjadi nilai numerik (A = 0, B = 1, dst.)
            char_num = ord(char.upper()) - 65
            # Hitung nilai numerik karakter terenkripsi dengan menggunakan rumus Vigenere Cipher
            new_char_num = (char_num + key_num[i % key_length]) % 26
            # Konversi nilai numerik terenkripsi menjadi karakter
            new_char = chr(new_char_num + 65)
            ciphertext += new_char
        else:
            ciphertext += char
    return ciphertext

# Fungsi untuk mendekripsi pesan dengan menggunakan Vigenere Cipher
def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)
    # Konversi karakter kunci menjadi nilai numerik (A = 0, B = 1, dst.)
    key_num = [ord(k.upper()) - 65 for k in key]
    # Dekripsi setiap karakter pada ciphertext dengan menggunakan nilai numerik kunci yang sesuai
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            # Konversi karakter terenkripsi menjadi nilai numerik (A = 0, B = 1, dst.)
            char_num = ord(char.upper()) - 65
            # Hitung nilai numerik karakter terdekripsi dengan menggunakan rumus Vigenere Cipher
            new_char_num = (char_num - key_num[i % key_length]) % 26
            # Konversi nilai numerik terdekripsi menjadi karakter
            new_char = chr(new_char_num + 65)
            plaintext += new_char
        else:
            plaintext += char
    return plaintext

# Contoh penggunaan Vigenere Cipher
plaintext = "EH Bukan 25 TAPI 225"
key = "QWERTYUIOPLKJHGFDSZXCVBNMA"
ciphertext = vigenere_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decrypted_text = vigenere_decrypt(ciphertext, key)
print("Plaintext:", decrypted_text)
