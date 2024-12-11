import tkinter as tk

from tkinter import *
from tkinter import messagebox
import customtkinter
import tkinter.font as tkFont
import random
customtkinter.set_appearance_mode("dark")


def center_window(window, width=2560, height=1600):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")
root = customtkinter.CTk()
root.title("Bezpieczeństwo systemów informatycznych")
center_window(root, 700, 700)
title_bar = tk.Frame(root, bg='black', relief='raised', bd=2)
title_bar.pack(fill='x')
default_font =tkFont.Font(family="helvetica",size=16)
root.option_add("*Font", default_font)


frame_encrypt = Frame(root, bg="black")
frame_encrypt.pack(fill="both",expand=True, padx=0, pady=0)

label_cipher = Label(frame_encrypt, text="Wybierz rodzaj szyfru", bg="black",fg="white")
label_cipher.grid(row=0, columnspan=5, pady=20)

cipher_buttons = []
polish_alphabet = [
    'a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń',
    'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ż', 'ź'
]
alphabet_length = len(polish_alphabet)
result_label = None
error_label = None
button_do = None
button_back = None
def encryption_menu():
    global result_label, error_label, button_do, button_back
    if result_label:
        result_label.grid_forget()
    if error_label:
        error_label.grid_forget()
    if button_do:
        button_do.grid_forget()
    if button_back:
        button_back.grid_forget()
    for widget in frame_encrypt.winfo_children():
        widget.grid_forget()
    for button in cipher_buttons:
        button.grid(row=20, column=cipher_buttons.index(button), padx=5, pady=5, sticky="ew")
    label_cipher.config(text="Wybierz rodzaj szyfru")
    label_cipher.grid(row=0, columnspan=5, pady=20)

def hide_buttons(buttons):
    for button in buttons:
        button.grid_forget()


def hides_buttons(buttons):
    for a in buttons:
        a.grid_forget()
#Cezar
def cipher_cezara(text, key):
    result = ""
    for char in text.lower():
        if char in polish_alphabet:
            index = polish_alphabet.index(char)
            new_index = (index + key) % len(polish_alphabet)
            result += polish_alphabet[new_index]
        else:
            result += char

    return result
def decipher_cezara(text, key):
    result = ""
    for char in text.lower():
        if char in polish_alphabet:
            index = polish_alphabet.index(char)
            new_index = (index - key) % len(polish_alphabet)
            result += polish_alphabet[new_index]
        else:
            result += char
    return result
def on_button_cipher_cezar():
    global result_label, error_label
    label_cipher.config(text="Szyfr Cezara")
    hides_buttons(cipher_buttons)

    label_input_cipher = Label(frame_encrypt, text="Wprowadź tekst do zaszyfrowania:", bg="black",fg="white")
    label_input_cipher.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    text_input_cipher = Entry(frame_encrypt, width=40,bg="lightgray" )
    text_input_cipher.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

    label_key_cipher = Label(frame_encrypt, text="Wprowadź klucz (1-34):", bg="black",fg="white")
    label_key_cipher.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    key_input_cipher = Entry(frame_encrypt, width=5,bg="lightgray" )
    key_input_cipher.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    def do_encryption():
        global result_label, error_label
        if result_label:
            result_label.grid_forget()
        if error_label:
            error_label.grid_forget()
        text = text_input_cipher.get()
        try:
            key_input = key_input_cipher.get()
            if key_input == "":
                raise ValueError("Klucz nie może być pusty.")
            if not key_input.isdigit():
                raise ValueError("W polu klucz mogą być tylko liczby dodatnie.")
            key = int(key_input)
            if key < 1 or key > 34:
                raise ValueError("Klucz musi być w zakresie od 1 do 34.")
            encrypted = cipher_cezara(text, key)
            if text != "":
                result_label = Label(frame_encrypt, text=f"Zaszyfrowany tekst: {encrypted}", bg="green",cursor="hand2")
                result_label.grid(row=4, column=0, columnspan=5, pady=10)
                result_label.bind("<Button-1>", lambda e: copy_to_clipboard(encrypted))
            else:
                error_label = Label(frame_encrypt, text="Błąd: Wprowadź dane.", bg="red")
                error_label.grid(row=4, column=0, columnspan=5, pady=10)
        except ValueError as ve:
            error_label = Label(frame_encrypt, text=f"Błąd: {ve}", bg="red")
            error_label.grid(row=4, column=0, columnspan=5, pady=10)

    button_do_cipher = tk.Button(frame_encrypt, text="szyfruj", command=do_encryption,bg="lightgray" )
    button_do_cipher.grid(row=3, column=2, padx=5, pady=5, sticky="ew")

    label_cipher.config(text="Szyfr Cezara")
    label_input_decipher = Label(frame_encrypt, text="Wprowadź Zaszyfrowany tekst:", bg="black",fg="white")
    label_input_decipher.grid(row=10, column=0, padx=5, pady=10, sticky="w")

    text_input_decipher = Entry(frame_encrypt, width=40,bg="lightgray" )
    text_input_decipher.grid(row=10, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

    label_key_decipher = Label(frame_encrypt, text="Wprowadź klucz (1-34):", bg="black",fg="white")
    label_key_decipher.grid(row=13, column=0, padx=5, pady=10, sticky="w")
    key_input_decipher = Entry(frame_encrypt, width=5 ,bg="lightgray" )
    key_input_decipher.grid(row=13, column=1, padx=5, pady=10, sticky="w")
    def perform_decryption():
        global result_label, error_label
        if result_label:
            result_label.grid_forget()
        if error_label:
            error_label.grid_forget()
        text = text_input_decipher.get()
        try:
            key_input = key_input_decipher.get()
            if key_input == "":
                raise ValueError("Klucz nie może być pusty.")
            if not key_input.isdigit():
                raise ValueError("W polu klucz mogą być tylko liczby dodatnie.")
            key = int(key_input)
            if key < 1 or key > 34:
                raise ValueError("Klucz musi być w zakresie od 1 do 34.")
            decryption = decipher_cezara(text, key)
            if text != "":
                result_label = Label(frame_encrypt, text=f"Zdeszyfrowany tekst: {decryption}", bg="green")
                result_label.grid(row=15, column=0, columnspan=5, pady=10)
            else:
                error_label = Label(frame_encrypt, text="Błąd: Wprowadź dane.", bg="red")
                error_label.grid(row=15, column=0, columnspan=5, pady=10)
        except ValueError as ve:
            error_label = Label(frame_encrypt, text=f"Błąd: {ve}", bg="red")
            error_label.grid(row=15, column=0, columnspan=5, pady=10)

    button_do_decipher = tk.Button(frame_encrypt, text="Deszyfruj", command=perform_decryption,bg="lightgray")
    button_do_decipher.grid(row=13, column=2, padx=5, pady=5, sticky="ew")

    button_back = tk.Button(frame_encrypt, text="Powrót do Menu", command=encryption_menu, width=25,
                               bg="lightgreen")
    button_back.grid(row=20, column=0, columnspan=5, pady=10)
#Polibiusz
def generate_random_polibiusz_table():
    shuffled = polish_alphabet.copy()
    random.shuffle(shuffled)
    table = [shuffled[i:i + 7] for i in range(0, 35, 7)]
    return table
def encrypt_polibiusz(text, table):
    cipher_text = ""
    for char in text.lower():
        found = False
        for i, row in enumerate(table):
            if char in row:
                j = row.index(char)
                cipher_text += f"{i+1}{j+1} "
                found = True
                break
        if not found:
            cipher_text += "? "
    return cipher_text.strip()
def decipher_polibiusz(cipher_text, table):
    deciphered_text = ""
    pairs = cipher_text.split()
    for pair in pairs:
        if len(pair) == 2:
            i = int(pair[0]) - 1
            j = int(pair[1]) - 1
            if 0 <= i < len(table) and 0 <= j < len(table[i]):
                deciphered_text += table[i][j]
            else:
                deciphered_text += "?"
    return deciphered_text
def on_button_cipher_polibiusz():
    global result_label, error_label,table

    label_cipher.config(text="Szyfr Polibiusza")
    hides_buttons(cipher_buttons)

    label_input_cipher = Label(frame_encrypt, text="Wprowadź tekst do zaszyfrowania:", bg="black", fg="white")
    label_input_cipher.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    text_input_cipher = Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_cipher.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

    label_key_cipher = Label(frame_encrypt, text="Wprowadź klucz (1-34):", bg="black",fg="white")
    label_key_cipher.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    key_input_cipher = Entry(frame_encrypt, width=5,bg="lightgray" )
    key_input_cipher.grid(row=3, column=1, padx=5, pady=5, sticky="w")


    table = generate_random_polibiusz_table()
    label_table = Label(frame_encrypt, text="Wygenerowana Tabela Polibiusza:", bg="black", fg="white")
    label_table.grid(row=5, column=1, padx=5, pady=5, sticky="w")

    table_frame = tk.Frame(frame_encrypt, bg="black")
    table_frame.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

    for i, row in enumerate(table):
        for j, char in enumerate(row):
            cell = Label(table_frame, text=char, bg="white", width=4, height=2)
            cell.grid(row=i, column=j, padx=2, pady=2)

    global result_label
    result_label = Label(frame_encrypt, text="", bg="black", fg="white")

    result_label.grid(row=7, column=0, columnspan=5, pady=10)
    label_input_decipher = Label(frame_encrypt, text="Wprowadź tekst do deszyfrowania:", bg="black", fg="white")
    label_input_decipher.grid(row=10, column=0, padx=5, pady=5, sticky="w")

    text_input_decipher = Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_decipher.grid(row=10, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

    label_key_decipher = Label(frame_encrypt, text="Wprowadź klucz (1-34):", bg="black", fg="white")
    label_key_decipher.grid(row=11, column=0, padx=5, pady=5, sticky="w")

    key_input_decipher = Entry(frame_encrypt, width=5, bg="lightgray")
    key_input_decipher.grid(row=11, column=1, padx=5, pady=5, sticky="w")

    def encrypt():
        text = text_input_cipher.get()
        if not text:
            messagebox.showerror("Błąd", "Wprowadź tekst do zaszyfrowania")
            return
        try:
            key = int(key_input_cipher.get())
            if key < 1 or key > 34:
                raise ValueError
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawny klucz (liczba całkowita od 1-34)")
            return

        cesar_text = cipher_cezara(text, key)
        encrypted_text = encrypt_polibiusz(cesar_text, table)
        result_label = Label(frame_encrypt, text=f"Zaszyfrowany tekst: {encrypted_text}", bg="green")
        result_label.grid(row=4, column=0, columnspan=5, pady=10)
        result_label.bind("<Button-1>", lambda e: copy_to_clipboard(encrypted_text))

    button_cipher = tk.Button(frame_encrypt, text="Szyfruj", command=encrypt, width=25, bg="lightblue")
    button_cipher.grid(row=8, column=1, columnspan=3, pady=10)
    def decipher():
        decrypted_text = text_input_decipher.get()
        if not decrypted_text:
            messagebox.showerror("Błąd", "Wprowadź zaszyfrowany tekst do odszyfrowania")
            return
        try:
            key = int(key_input_decipher.get())
            if key < 1 or key > 34:
                raise ValueError
        except ValueError:
            messagebox.showerror("Błąd", "Wprowadź poprawny klucz (liczba całkowita) od 1-34")
            return

        decrypted_cypher_text = decipher_polibiusz(decrypted_text, table)
        decrypted_text = decipher_cezara(decrypted_cypher_text, key)
        result_label=Label(frame_encrypt,text=f"Odszyfrowany tekst: {decrypted_text}",bg="green")
        result_label.grid(row=14,column=0,columnspan=3, pady=10)


    button_decrypt = tk.Button(frame_encrypt, text="Deszyfruj", command=decipher, width=25, bg="lightblue")
    button_decrypt.grid(row=15, column=1, columnspan=3, pady=10)

    button_back = tk.Button(frame_encrypt, text="Powrót do Menu", command=encryption_menu, width=25,
                              bg="lightgreen")
    button_back.grid(row=20, column=0, columnspan=5, pady=10)
#Vigenere
def encrypt_vigenere(plaintext, key):
    ciphertext = []
    key_length = len(key)
    plaintext_int = [polish_alphabet.index(char) for char in plaintext]
    key_int = [polish_alphabet.index(char) for char in key]

    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_int[i % key_length]) % alphabet_length
        ciphertext.append(polish_alphabet[value])

    return ''.join(ciphertext)
def decrypt_vigenere(ciphertext, key):
    plaintext = []
    key_length = len(key)

    ciphertext_int = [polish_alphabet.index(char) for char in ciphertext]
    key_int = [polish_alphabet.index(char) for char in key]

    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_int[i % key_length]) % alphabet_length
        plaintext.append(polish_alphabet[value])

    return ''.join(plaintext)
def on_button_cipher_vigenere():
    global result_label, error_label, table
    label_cipher.config(text="Szyfr FairPlay")
    hides_buttons(cipher_buttons)
    label_input_cipher = Label(frame_encrypt, text="Wprowadź tekst do zaszyfrowania:", bg="black", fg="white")
    label_input_cipher.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    text_input_cipher = Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_cipher.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

    label_input_key = Label(frame_encrypt, text="Klucz:", bg="black", fg="white")
    label_input_key.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    text_input_key = Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_key.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

    def encrypt():
        text = text_input_cipher.get()
        key = text_input_key.get()
        if not text:
            messagebox.showerror("Błąd", "Wprowadź tekst do zaszyfrowania")
            return
        if not key or not key.isalpha():
            messagebox.showerror("Błąd", "Wprowadź Klucz,nie mogą być liczby")
            return
        encrypt_text = encrypt_vigenere(text,key)
        result_label = Label(frame_encrypt, text=f"Zaszyfrowany tekst: {encrypt_text}", bg="green")
        result_label.grid(row=4, column=0, columnspan=5, pady=10)
        result_label.bind("<Button-1>", lambda e: copy_to_clipboard(encrypt_text))

    button_encrypt = tk.Button(frame_encrypt, text="Szyfruj", command=encrypt, width=25, bg="lightblue")
    button_encrypt.grid(row=5, column=1, columnspan=5, pady=10)

    label_input_decipher = Label(frame_encrypt, text="Wprowadź tekst do dzeszyfrowania:", bg="black", fg="white")
    label_input_decipher.grid(row=6, column=0, padx=5, pady=5, sticky="w")

    text_input_decipher = Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_decipher.grid(row=6, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

    label_input_key_decipher = Label(frame_encrypt, text="Klucz:", bg="black", fg="white")
    label_input_key_decipher.grid(row=7, column=0, padx=5, pady=5, sticky="w")

    text_input_key_decipher = Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_key_decipher.grid(row=7, column=1, columnspan=3, padx=5, pady=5, sticky="ew")
    def decipher():
        text = text_input_decipher.get()
        key = text_input_key_decipher.get()
        if not text:
            messagebox.showerror("Błąd", "Wprowadź tekst do zaszyfrowania")
            return
        if not key or not key.isalpha():
            messagebox.showerror("Błąd", "Wprowadź Klucz,nie mogą być liczby")
            return
        decrypted_text= decrypt_vigenere(text,key)
        result_label = Label(frame_encrypt, text=f"Odszyfrowany tekst: {decrypted_text}", bg="green")
        result_label.grid(row=8, column=0, columnspan=5, pady=10)


    button_decrypted = tk.Button(frame_encrypt, text="Deszyfruj", command=decipher, width=25, bg="lightblue")
    button_decrypted.grid(row=9, column=1, columnspan=5, pady=10)
    global button_back
    button_back = tk.Button(frame_encrypt, text="Powrót do Menu",command=encryption_menu, width=25, bg="lightgreen")
    button_back.grid(row=10, column=0, columnspan=5, pady=10)
def generate_matrix(key):
    matrix = []
    added_letters = set()

    # Dodajemy litery z klucza do macierzy, upewniając się, że są w alfabecie
    for letter in key.lower():
        if letter not in added_letters and letter in polish_alphabet:
            matrix.append(letter)
            added_letters.add(letter)

    # Dodajemy resztę liter z polskiego alfabetu, jeśli nie zostały dodane
    for letter in polish_alphabet:
        if letter not in added_letters:
            matrix.append(letter)

    # Zwracamy macierz o szerokości 5
    return [matrix[i:i + 5] for i in range(0, len(matrix), 5)]
def create_digraphs(text):
    text = text.lower().replace(" ", "")
    text = ''.join([char for char in text if char in polish_alphabet])

    digraphs = []
    i = 0
    while i < len(text):
        letter1 = text[i]
        if i + 1 < len(text):
            letter2 = text[i + 1]
            if letter1 == letter2:
                digraphs.append((letter1, 'x'))
                i += 1
            else:
                digraphs.append((letter1, letter2))
                i += 2
        else:
            digraphs.append((letter1, 'x'))
            i += 1
    return digraphs
def find_position(letter, matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == letter:
                return row, col
    raise ValueError(f"Letter '{letter}' not found in matrix")
def encrypt_digraph(digraph, matrix):
    row1, col1 = find_position(digraph[0], matrix)
    row2, col2 = find_position(digraph[1], matrix)

    if row1 == row2:
        col1 = (col1 + 1) % 5
        col2 = (col2 + 1) % 5
    elif col1 == col2:
        row1 = (row1 + 1) % 7
        row2 = (row2 + 1) % 7
    else:
        col1, col2 = col2, col1

    return matrix[row1][col1] + matrix[row2][col2]
def decrypt_digraph(digraph, matrix):
    row1, col1 = find_position(digraph[0], matrix)
    row2, col2 = find_position(digraph[1], matrix)

    if row1 == row2:
        col1 = (col1 - 1) % 5
        col2 = (col2 - 1) % 5
    elif col1 == col2:
        row1 = (row1 - 1) % 7
        row2 = (row2 - 1) % 7
    else:
        col1, col2 = col2, col1

    return matrix[row1][col1] + matrix[row2][col2]
def playfair_encrypt(text, key):
    matrix = generate_matrix(key)
    digraphs = create_digraphs(text)
    ciphertext = ""

    for digraph in digraphs:
        ciphertext += encrypt_digraph(digraph, matrix)

    return ciphertext
def playfair_decrypt(ciphertext, key):
    matrix = generate_matrix(key)
    digraphs = create_digraphs(ciphertext)
    plaintext = ""

    for digraph in digraphs:
        plaintext += decrypt_digraph(digraph, matrix)

    return plaintext
def on_button_fairplay():
    global result_label
    label_cipher.config(text="Szyfr FairPlay")
    hides_buttons(cipher_buttons)

    label_input_cipher = tk.Label(frame_encrypt, text="Wprowadź tekst do zaszyfrowania:", bg="black", fg="white")
    label_input_cipher.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    text_input_cipher = tk.Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_cipher.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

    label_input_key = tk.Label(frame_encrypt, text="Klucz:", bg="black", fg="white")
    label_input_key.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    text_input_key = tk.Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_key.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

    def encrypt():
        text = text_input_cipher.get()
        key = text_input_key.get()
        if not text:
            messagebox.showerror("Błąd", "Wprowadź tekst do zaszyfrowania")
            return
        if not key or not key.isalpha():
            messagebox.showerror("Błąd", "Wprowadź Klucz, nie mogą być liczby")
            return
        encrypt_text = playfair_encrypt(text, key)

        if not encrypt_text:
            messagebox.showerror("Błąd", "Błąd w szyfrowaniu, spróbuj ponownie.")
            return

        result_label = tk.Label(frame_encrypt, text=f"Zaszyfrowany tekst: {encrypt_text}", bg="green")
        result_label.grid(row=4, column=0, columnspan=5, pady=10)
        result_label.bind("<Button-1>", lambda e: copy_to_clipboard(encrypt_text))

    button_encrypt = tk.Button(frame_encrypt, text="Szyfruj", command=encrypt, width=25, bg="lightblue")
    button_encrypt.grid(row=5, column=1, columnspan=5, pady=10)

    label_input_decipher = tk.Label(frame_encrypt, text="Wprowadź tekst do deszyfrowania:", bg="black", fg="white")
    label_input_decipher.grid(row=6, column=0, padx=5, pady=5, sticky="w")

    text_input_decipher = tk.Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_decipher.grid(row=6, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

    label_input_key_decipher = tk.Label(frame_encrypt, text="Klucz:", bg="black", fg="white")
    label_input_key_decipher.grid(row=7, column=0, padx=5, pady=5, sticky="w")

    text_input_key_decipher = tk.Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_key_decipher.grid(row=7, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

    def decipher():
        text = text_input_decipher.get()
        key = text_input_key_decipher.get()
        if not text:
            messagebox.showerror("Błąd", "Wprowadź tekst do deszyfrowania")
            return
        if not key or not key.isalpha():
            messagebox.showerror("Błąd", "Wprowadź Klucz, nie mogą być liczby")
            return
        decrypted_text = playfair_decrypt(text, key)


        result_label = tk.Label(frame_encrypt, text=f"Odszyfrowany tekst: {decrypted_text}", bg="green")
        result_label.grid(row=8, column=0, columnspan=5, pady=10)

    button_decrypted = tk.Button(frame_encrypt, text="Deszyfruj", command=decipher, width=25, bg="lightblue")
    button_decrypted.grid(row=9, column=1, columnspan=5, pady=10)

    button_back = tk.Button(frame_encrypt, text="Powrót do Menu", command=encryption_menu, width=25, bg="lightgreen")
    button_back.grid(row=10, column=0, columnspan=5, pady=10)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def find_e(phi):
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            return e
        e += 1
    raise ValueError("Nie znaleziono odpowiedniego e.")
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("Nie znaleziono odwrotności modularnej.")
def text_to_int(text):

    return int(''.join(f"{ord(c):05}" for c in text))
def int_to_text(number):

    number_str = str(number)
    text = ''.join(chr(int(number_str[i:i+5])) for i in range(0, len(number_str), 5))
    return text
def czy_pierwsza(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def copy_to_clipboard(text):
    original_text = result_label.cget("text")
    original_bg = result_label.cget("bg")

    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

    result_label.config(text="Zaszyfrowany tekst został skopiowany!", bg="yellow")


    root.after(1000, lambda: result_label.config(text=original_text, bg=original_bg))
def on_button_RSA():
    global result_label
    label_cipher.config(text="Szyfr RSA")
    hides_buttons(cipher_buttons)

    label_input_cipher = tk.Label(frame_encrypt, text="Wprowadź tekst do zaszyfrowania:", bg="black", fg="white")
    label_input_cipher.grid(row=2, column=0, padx=5, pady=5, sticky="w")

    text_input_cipher = tk.Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_cipher.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

    label_input_key_p = tk.Label(frame_encrypt, text="Podaj liczbę pierwszą p:", bg="black", fg="white")
    label_input_key_p.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    text_input_key_p = tk.Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_key_p.grid(row=3, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

    label_input_key_q = tk.Label(frame_encrypt, text="Podaj liczbę pierwszą q:", bg="black", fg="white")
    label_input_key_q.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    text_input_key_q = tk.Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_key_q.grid(row=4, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

    def encrypt():
        global result_label
        text = text_input_cipher.get()
        if not text:
            messagebox.showerror("Błąd", "Wprowadź tekst do zaszyfrowania")
            return
        try:
            key_p = int(text_input_key_p.get())
            key_q = int(text_input_key_q.get())
        except ValueError:
            messagebox.showerror("Błąd", "Podaj poprawne liczby pierwsze")
            return

        if not czy_pierwsza(key_p):
            messagebox.showerror("Błąd", "Podaj liczbę pierwszą dla p")
            return
        elif not czy_pierwsza(key_q):
            messagebox.showerror("Błąd", "Podaj liczbę pierwszą dla q")
            return

        n = key_p * key_q
        phi = (key_p - 1) * (key_q - 1)

        e = find_e(phi)
        d = modinv(e, phi)

        encrypted_message = []
        for char in text:
            char_code = ord(char)
            encrypted_char = pow(char_code, e, n)
            encrypted_message.append(str(encrypted_char))

        encrypted_text = " ".join(encrypted_message)

        result_label = tk.Label(frame_encrypt, text=f"Klucz publiczny: e={e}, n={n}\n"
                                                    f"Klucz prywatny: d={d}, n={n}\n"
                                                    f"Zaszyfrowany tekst: {encrypted_text}", bg="green",cursor="hand2")
        result_label.grid(row=5, column=0, columnspan=5, pady=10)
        result_label.bind("<Button-1>", lambda e: copy_to_clipboard(encrypted_text))

    button_encrypt = tk.Button(frame_encrypt, text="Szyfruj", command=encrypt, width=25, bg="lightblue")
    button_encrypt.grid(row=7, column=1, columnspan=5, pady=10)

    label_input_decipher = tk.Label(frame_encrypt, text="Wprowadź Zaszyfrowany tekst:", bg="black", fg="white")
    label_input_decipher.grid(row=8, column=0, padx=5, pady=5, sticky="w")

    text_input_decipher = tk.Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_decipher.grid(row=8, column=1, columnspan=3, padx=5, pady=5, sticky="ew")

    label_input_key_decipher = tk.Label(frame_encrypt, text="Wpisz klucz prywatny:", bg="black", fg="white")
    label_input_key_decipher.grid(row=9, column=0, padx=5, pady=5, sticky="w")

    text_input_key_d = tk.Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_key_d.grid(row=10, column=0, padx=5, pady=5, sticky="w")
    text_input_key_n = tk.Entry(frame_encrypt, width=40, bg="lightgray")
    text_input_key_n.grid(row=11, column=0, padx=5, pady=5, sticky="w")

    def decipher():
        encrypted_text = text_input_decipher.get()
        if not encrypted_text:
            messagebox.showerror("Błąd", "Wprowadź zaszyfrowany tekst")
            return
        try:
            key_d = int(text_input_key_d.get())
            key_n = int(text_input_key_n.get())
        except ValueError:
            messagebox.showerror("Błąd", "Klucz może być tylko liczbami")
            return

        encrypted_chars = encrypted_text.split()
        decrypted_message = ""

        for encrypted_char in encrypted_chars:
            try:
                encrypted_char = int(encrypted_char)
            except ValueError:
                messagebox.showerror("Błąd", "Zaszyfrowany tekst musi składać się z liczb oddzielonych spacjami")
                return

            decrypted_char = pow(encrypted_char, key_d, key_n)
            decrypted_message += chr(decrypted_char)

        result_label = tk.Label(frame_encrypt, text=f"Odszyfrowany tekst: {decrypted_message}", bg="green")
        result_label.grid(row=12, column=0, columnspan=5, pady=10)

    button_decrypted = tk.Button(frame_encrypt, text="Deszyfruj", command=decipher, width=25, bg="lightblue")
    button_decrypted.grid(row=11, column=1, columnspan=5, pady=10)

    button_back = tk.Button(frame_encrypt, text="Powrót do Menu", command=encryption_menu, width=25, bg="lightgreen")
    button_back.grid(row=14, column=0, columnspan=5, pady=10)
#Menu
total_rows = 50
for row in range(total_rows):
    frame_encrypt.grid_rowconfigure(row, weight=1)

button_cezar = Button(frame_encrypt, text="Szyfr Cezara", command=on_button_cipher_cezar, width=15,bg="darkgray",fg="black")
button_cezar.grid(row=20, column=0, padx=20, pady=10, sticky="ew")
cipher_buttons.append(button_cezar)

button_polibiusz = Button(frame_encrypt, text="Szyfr Polibiusza ", command=on_button_cipher_polibiusz, width=15,bg="darkgray",fg="black")
button_polibiusz.grid(row=20, column=1, padx=10, pady=10, sticky="ew")
cipher_buttons.append(button_polibiusz)

button = Button(frame_encrypt, text="Szyfr Vigenère’a", command=on_button_cipher_vigenere, width=15,bg="darkgray",fg="black")
button.grid(row=20, column=2, padx=20, pady=10, sticky="ew")
cipher_buttons.append(button)

button = Button(frame_encrypt, text="Szyfr FairPlay", command=on_button_fairplay, width=15,bg="darkgray",fg="black")
button.grid(row=20, column=3, padx=20, pady=10, sticky="ew")
cipher_buttons.append(button)

button = Button(frame_encrypt, text="Szyfr RSA", command=on_button_RSA, width=15,bg="darkgray",fg="black")
button.grid(row=20, column=4, padx=20, pady=10, sticky="ew")
cipher_buttons.append(button)

for i in range(5):
    frame_encrypt.grid_columnconfigure(i, weight=2)
root.mainloop() 