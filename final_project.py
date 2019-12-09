"""
Program: Hangman Game - Final Project
Author: Ryan Blankenship
Last date modified: 12/10/2019
"""
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

window = Tk()
window.title("Welcome to the Hangman Game")
window.config(bg="white")

words = ["PYTHON", "COMMENTS", "VARIABLES", "NUMBERS", "CASTING", "STRINGS", "BOOLEANS",
         "OPERATORS", "LISTS", "TUPLES", "SETS", "DICTIONARIES", "LOOPS", "FUNCTIONS", "ARRAYS",
         "CLASSES", "OBJECTS", "INHERITANCE", "ITERATORS", "SCOPE", "MODULES", "UNITTESTING",
         "DOCSTRING"]

hangman_photos = [PhotoImage(file="images/image_0.png"), PhotoImage(file="images/image_1.png"),
                  PhotoImage(file="images/image_2.png"), PhotoImage(file="images/image_3.png"),
                  PhotoImage(file="images/image_4.png"), PhotoImage(file="images/image_5.png"),
                  PhotoImage(file="images/image_6.png"), PhotoImage(file="images/image_7.png")]


def start_game():
    global letter_in_word_with_space
    global number_of_guesses
    number_of_guesses = 0
    photo_label.configure(image=hangman_photos[0])
    secret_word = random.choice(words)
    letter_in_word_with_space = " ".join(secret_word)
    join_letters_in_word.set(" ".join("_" * len(secret_word)))


def guess(letter):
    global number_of_guesses
    if number_of_guesses < 7:
        text = list(letter_in_word_with_space)
        guessed = list(join_letters_in_word.get())
        if letter_in_word_with_space.count(letter) > 0:
            for alpha in range(len(text)):
                if text[alpha] == letter:
                    guessed[alpha] = letter
                join_letters_in_word.set("".join(guessed))
                if join_letters_in_word.get() == letter_in_word_with_space:
                    messagebox.showinfo("Hangman", "You did it!")
        else:
            number_of_guesses += 1
            photo_label.config(image=hangman_photos[number_of_guesses])
            if number_of_guesses == 5:
                messagebox.showwarning("Chances Remaining", "Only 2 more guesses left")
            elif number_of_guesses == 6:
                messagebox.showwarning("Chances Remaining", "Only 1 more guesses left")
            elif number_of_guesses == 7:
                messagebox.showwarning("Hangman", "Sorry, game over")


photo_label = Label(window, bg="white")
photo_label.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
photo_label.configure(image=hangman_photos[0])

join_letters_in_word = StringVar()
Label(window, textvariable=join_letters_in_word, font="Consolas 24 bold", bg="white").grid(row=0, column=3, columnspan=6, padx=10)

n = 0
for alpha in ascii_uppercase:
    Button(window, text=alpha, command=lambda a=alpha: guess(a), font="Helvetica 18", bg="white", height=2, width=5).grid(
        row=1 + n // 9,
        column=n % 9)
    n += 1

Button(window, text="New\nGame", command=lambda: start_game(), font="Helvetica 12 bold", bg="red", fg="white").grid(row=3,
                                                                                                                    column=8,
                                                                                                                    sticky="NSWE")
start_game()
window.mainloop()
