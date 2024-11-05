import tkinter as tk

from tkinter import *
from tkinter import messagebox
import numpy as np
import customtkinter
import tkinter.font as tkFont
import random
from PIL import Image, ImageTk, ImageDraw
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
def on_button_cipher():
    label_cipher.config(text="Wkrótce")
    hide_buttons(cipher_buttons)
    global button_back
    button_back = tk.Button(frame_encrypt, text="Powrót do Menu",
                              command=encryption_menu, width=25, bg="lightblue")
    button_back.grid(row=5, column=0, columnspan=5, pady=10)

def hide_buttons(buttons):
    for button in buttons:
        button.grid_forget()
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
    hide_buttons(cipher_buttons)

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
                result_label = Label(frame_encrypt, text=f"Zaszyfrowany tekst: {encrypted}", bg="green")
                result_label.grid(row=4, column=0, columnspan=5, pady=10)
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
    hide_buttons(cipher_buttons)

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
    hide_buttons(cipher_buttons)
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

def on_button_fairplay():
    global result_label, error_label, table
    label_cipher.config(text="Szyfr Vigenère’a")
    hide_buttons(cipher_buttons)
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
        encrypt_text = encrypt_vigenere(text, key)
        result_label = Label(frame_encrypt, text=f"Zaszyfrowany tekst: {encrypt_text}", bg="green")
        result_label.grid(row=4, column=0, columnspan=5, pady=10)

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
        decrypted_text = decrypt_vigenere(text, key)
        result_label = Label(frame_encrypt, text=f"Odszyfrowany tekst: {decrypted_text}", bg="green")
        result_label.grid(row=8, column=0, columnspan=5, pady=10)

    button_decrypted = tk.Button(frame_encrypt, text="Deszyfruj", command=decipher, width=25, bg="lightblue")
    button_decrypted.grid(row=9, column=1, columnspan=5, pady=10)
    global button_back
    button_back = tk.Button(frame_encrypt, text="Powrót do Menu", command=encryption_menu, width=25, bg="lightgreen")
    button_back.grid(row=10, column=0, columnspan=5, pady=10)


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

button = Button(frame_encrypt, text="Szyfr ?", command=on_button_cipher, width=15,bg="darkgray",fg="black")
button.grid(row=20, column=4, padx=20, pady=10, sticky="ew")
cipher_buttons.append(button)

for i in range(5):
    frame_encrypt.grid_columnconfigure(i, weight=2)
root.mainloop() 