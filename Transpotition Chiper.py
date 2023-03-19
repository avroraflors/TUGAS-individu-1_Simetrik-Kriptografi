def encrypt(message, key):
    # Menentukan jumlah baris
    num_of_rows = len(message) // key
    if len(message) % key:
        num_of_rows += 1

    # Menambahkan karakter padding jika diperlukan
    message += ' ' * (num_of_rows * key - len(message))

    # Membuat matriks untuk pesan yang dienkripsi
    ciphertext = [''] * key
    for col in range(key):
        for row in range(num_of_rows):
            index = row * key + col
            ciphertext[col] += message[index]

    # Menggabungkan baris menjadi pesan yang dienkripsi
    return ''.join(ciphertext)

def decrypt(ciphertext, key):
    # Menentukan jumlah baris
    num_of_rows = len(ciphertext) // key

    # Membuat matriks untuk pesan asli yang didekripsi
    plaintext = [''] * num_of_rows
    for row in range(num_of_rows):
        for col in range(key):
            index = row + col * num_of_rows
            plaintext[row] += ciphertext[index]

    # Menghapus karakter padding dan mengembalikan pesan asli yang didekripsi
    return plaintext[0].rstrip()

# Contoh penggunaan
message = 'Ini adalah pesan yang akan dienkripsi'
key =24

ciphertext = encrypt(message, key)
print('Pesan yang dienkripsi:', ciphertext)

plaintext = decrypt(ciphertext, key)
print('Pesan asli yang didekripsi:', plaintext)
