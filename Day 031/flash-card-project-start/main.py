import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
BLACK = "#000000"
WHITE = "#ffffff"


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    italian_card()
    timer = window.after(3000, func=english_card)
    to_learn.remove(current_card)
    new_data = data.from_dict(to_learn, orient="columns")
    new_data.to_csv('data/words_to_learn.csv', index=False)


def italian_card():
    canvas.itemconfig(background, image=card_front_img)
    canvas.itemconfig(card_title, text='Italian', fill=BLACK)
    canvas.itemconfig(card_word, text=current_card['Italian'], fill=BLACK)


def english_card():
    canvas.itemconfig(background, image=card_back_img)
    canvas.itemconfig(card_title, text='English', fill=WHITE)
    canvas.itemconfig(card_word, text=current_card['English'], fill=WHITE)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    base_data = pandas.read_csv("data/italian_words.csv")
    base_data.to_csv("data/words_to_learn.csv", index=False)
    data = pandas.read_csv("data/words_to_learn.csv")
finally:
    to_learn = data.to_dict(orient="records")


current_card = {}

timer = window.after(3000, func=english_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400, 263, image=card_front_img)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 125, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 250, text="word", font=('Arial', 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)


# ------------------------------ Code Above This ------------------------------ #
window.mainloop()
