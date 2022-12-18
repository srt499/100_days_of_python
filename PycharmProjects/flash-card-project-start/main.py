from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_learned = []

# ---------------------------- Get Words from CSV ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/japanese_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")


# ---------------------------- Create Cards, Flip ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    flashcard.itemconfig(title, text="Japanese", fill="black")
    flashcard.itemconfig(word, text=current_card['Japanese'], fill="black")
    flashcard.itemconfig(card_background, image=front_flash_img)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    flashcard.itemconfig(card_background, image=back_flash_img)
    flashcard.itemconfig(title, text="English", fill="white")
    flashcard.itemconfig(word, text=current_card["English"], fill="white")


def known_word():
    words_to_learn.remove(current_card)
    next_card()
    need_to_learn = pandas.DataFrame(words_to_learn)
    need_to_learn.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

flashcard = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_flash_img = PhotoImage(file='images/card_front.png')
back_flash_img = PhotoImage(file='images/card_back.png')
card_background = flashcard.create_image(400, 263, image=front_flash_img)
title = flashcard.create_text(400, 150, font=("Arial", 40, "italic"), text="")
word = flashcard.create_text(400, 263, font=("Arial", 60, "bold"), text="")
flashcard.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()

