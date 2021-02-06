# Packages
from tkinter import *
import pandas
import random

# Constants
BACKGROUNG_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Reads data
try:
    data = pandas.read_csv("support_files/words_to_learn.csv")
except FileNotFoundError:
    original_record = pandas.read_csv("support_files/spanish_to_english.csv")
    to_learn = original_record.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# Chooses next card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.config(bg="#ffffff")
    flip_timer = window.after(3000, func=flip_card)

# Flips card
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.config(card_background, bg="#D1DEC9")

# Removes the current word.
def is_known():
    to_learn.remove(current_card)
    update_words()
    next_card()

# Creates new data file
def update_words():
    data = pandas.DataFrame(to_learn)
    data.to_csv("support_files/words_to_learn.csv", index=False)

# Window creation
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUNG_COLOR)

# Shows the english word after 3 seconds
flip_timer = window.after(3000, func=flip_card)

# Canvas creation
canvas = Canvas(width=800, height=526)
card_title = canvas.create_text(400, 150, font="Ariel 40 italic", text="")
card_word = canvas.create_text(400, 263, font="Ariel 60 bold", text="")
card_background = canvas.config(bg="#ffffff", highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Button creation
unknown_button = Button(padx=20, pady=20, text="NO", highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)
known_button = Button(padx=20, pady=20, text="YES", highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# Helps to show the first word
next_card()

# Keeps the window open until closed manually
window.mainloop()
