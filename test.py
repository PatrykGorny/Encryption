
import tkinter as tk
from tkinter import *

def center_window(window, width=300, height=200):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.title("Bezpieczeństwo systemów informatycznych")
center_window(root, 1000, 400)


frame_szyfrowanie = Frame(root, bg="lightblue")
frame_szyfrowanie.pack(fill="both", expand=True, padx=10, pady=5)

frame_deszyfrowanie = Frame(root, bg="lightgreen")
frame_deszyfrowanie.pack(fill="both", expand=True, padx=10, pady=5)


label_szyfr = Label(frame_szyfrowanie, text="Wybierz rodzaj szyfrowania", bg="lightblue")
label_szyfr.grid(row=0, columnspan=5, pady=5)

label_deszyfr = Label(frame_deszyfrowanie, text="Wybierz rodzaj deszyfrowania", bg="lightgreen")
label_deszyfr.grid(row=0, columnspan=5, pady=5)

szyfr_buttons = []
polski_alfabet = [
    'a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń',
    'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ż', 'ź'
]


def szyfr_cezara(text, key):
    result = ""
    for char in text.lower():
        if char in polski_alfabet:
            index = polski_alfabet.index(char)
            new_index = (index + key) % len(polski_alfabet)
            result += polski_alfabet[new_index]
        else:
            result += char

    return result

wynik_label = None
error_label = None
button_wykonaj = None
button_powrot = None

def pokaz_przyciski_szyfrowania():
    global wynik_label, error_label, button_wykonaj, button_powrot
    # Ukrycie etykiet i pól do wprowadzania tekstu
    if wynik_label:
        wynik_label.grid_forget()
    if error_label:
        error_label.grid_forget()

    # Ukrycie pól do wprowadzania
    for widget in frame_szyfrowanie.grid_slaves():
        if isinstance(widget, (tk.Label, tk.Entry)):
            widget.grid_forget()

    # Ukrycie przycisków "Wykonaj szyfrowanie" i "Powrót do wyboru szyfrowania"
    if button_wykonaj:
        button_wykonaj.grid_forget()
    if button_powrot:
        button_powrot.grid_forget()

    # Wyświetlenie przycisków szyfrowania
    for button in szyfr_buttons:
        button.grid(row=1, column=szyfr_buttons.index(button), padx=5, pady=5, sticky="ew")

    # Przywrócenie etykiety
    label_szyfr.config(text="Wybierz rodzaj szyfrowania")

def on_button_szyfr_cezar():
    global wynik_label, error_label
    label_szyfr.config(text="Szyfrowanie Cezara wybrane")
    hide_buttons(szyfr_buttons)
    label_input = Label(frame_szyfrowanie, text="Wprowadź tekst do zaszyfrowania:", bg="lightblue")
    label_input.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    text_input = Entry(frame_szyfrowanie, width=40)
    text_input.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="ew")
    label_key = Label(frame_szyfrowanie, text="Wprowadź klucz (1-34):", bg="lightblue")
    label_key.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    key_input = Entry(frame_szyfrowanie, width=5)
    key_input.grid(row=3, column=1, padx=5, pady=5, sticky="w")

    def wykonaj_szyfrowanie():
        global wynik_label, error_label
        if wynik_label:
            wynik_label.grid_forget()
        if error_label:
            error_label.grid_forget()
        tekst = text_input.get()
        try:

            klucz_input = key_input.get()

            if klucz_input == "":
                raise ValueError("Wprowadź dane. Klucz nie może być pusty.")

            if not klucz_input.isdigit():
                raise ValueError("W polu klucz mogą być tylko liczby.")
            klucz = int(klucz_input)
            if klucz < 1 or klucz > 34:
                raise ValueError("Klucz musi być w zakresie od 1 do 34.")

            # Jeśli wszystko jest w porządku, zaszyfruj tekst
            zaszyfrowany = szyfr_cezara(tekst, klucz)

            # Sprawdzenie, czy tekst nie jest pusty
            if tekst != "":
                wynik_label = Label(frame_szyfrowanie, text=f"Zaszyfrowany tekst: {zaszyfrowany}", bg="lightblue")
                wynik_label.grid(row=4, column=0, columnspan=5, pady=10)
            else:
                error_label = Label(frame_szyfrowanie, text="Błąd: Wprowadź dane.", bg="red")
                error_label.grid(row=4, column=0, columnspan=5, pady=10)

        except ValueError as ve:
            # Utworzenie nowej etykiety błędu
            error_label = Label(frame_szyfrowanie, text=f"Błąd: {ve}", bg="red")
            error_label.grid(row=4, column=0, columnspan=5, pady=10)

    global button_wykonaj  # Używamy globalnej zmiennej dla przycisku
    button_wykonaj = tk.Button(frame_szyfrowanie, text="Wykonaj szyfrowanie", command=wykonaj_szyfrowanie)
    button_wykonaj.grid(row=3, column=2, padx=5, pady=5, sticky="ew")

    # Dodanie przycisku powrotu
    global button_powrot  # Używamy globalnej zmiennej dla przycisku
    button_powrot = tk.Button(frame_szyfrowanie, text="Powrót do Menu szyfrowania",
                              command=pokaz_przyciski_szyfrowania, width=25, font=("Arial", 12), bg="lightblue")
    button_powrot.grid(row=5, column=0, columnspan=5, pady=10)


# Funkcja tymczasowa dla innych szyfrowań
def on_button_szyfr():
    label_szyfr.config(text="Szyfrowanie ... wybrane")
    hide_buttons(szyfr_buttons)  # Ukrywamy przyciski po wybraniu opcji
    global button_powrot  # Używamy globalnej zmiennej dla przycisku
    button_powrot = tk.Button(frame_szyfrowanie, text="Powrót do Menu szyfrowania",
                              command=pokaz_przyciski_szyfrowania, width=25, font=("Arial", 12), bg="lightblue")
    button_powrot.grid(row=5, column=0, columnspan=5, pady=10)

# Funkcja do zmiany tekstu dla deszyfrowania Cezara
def on_button_deszyfr_cezar():
    label_deszyfr.config(text="Deszyfrowanie Cezara wybrane")
    hide_buttons(szyfr_buttons)

# Funkcja tymczasowa dla innych deszyfrowań
def on_button_deszyfr():
    label_deszyfr.config(text="Deszyfrowanie ... wybrane")

# Funkcja do ukrywania przycisków
def hide_buttons(buttons):
    for button in buttons:
        button.grid_forget()  # Ukrywamy każdy przycisk

# Przyciski dla sekcji szyfrowania
button1 = Button(frame_szyfrowanie, text="Szyfrowanie Cezara", command=on_button_szyfr_cezar, width=15)
button1.grid(row=1, column=0, padx=5, pady=5, sticky="ew")  # "ew" rozciąga przycisk w poziomie

szyfr_buttons.append(button1)  # Dodajemy do listy przycisków

# Dodajmy inne przyciski tymczasowe
for i in range(4):
    button_temp = Button(frame_szyfrowanie, text=f"Szyfrowanie {i+1} ...", command=on_button_szyfr, width=15)
    button_temp.grid(row=1, column=i+1, padx=5, pady=5, sticky="ew")  # Kolejne przyciski w tym samym wierszu
    szyfr_buttons.append(button_temp)  # Dodajemy każdy przycisk do listy

# Zarządzanie rozciąganiem kolumn w sekcji szyfrowania (teraz 5 kolumn)
for i in range(5):
    frame_szyfrowanie.grid_columnconfigure(i, weight=1)  # Sprawia, że kolumny są elastyczne

# Przyciski dla sekcji deszyfrowania
button2 = Button(frame_deszyfrowanie, text="Deszyfrowanie Cezara", command=on_button_deszyfr_cezar, width=15)
button2.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

# Dodajmy inne przyciski tymczasowe dla deszyfrowania
for i in range(4):
    button_temp = Button(frame_deszyfrowanie, text=f"Deszyfrowanie {i+1} ...", command=on_button_deszyfr, width=15)
    button_temp.grid(row=1, column=i+1, padx=5, pady=5, sticky="ew")

# Zarządzanie rozciąganiem kolumn w sekcji deszyfrowania (teraz 5 kolumn)
for i in range(5):
    frame_deszyfrowanie.grid_columnconfigure(i, weight=1)  # Sprawia, że kolumny są elastyczne

root.mainloop()
