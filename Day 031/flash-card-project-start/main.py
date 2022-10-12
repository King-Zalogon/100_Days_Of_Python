import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

data = pandas.read_csv("data/italian_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='Italian')
    canvas.itemconfig(card_word, text=current_card['Italian'])

def get_word():
    global word
    global title
    canvas.delete(word)
    word = canvas.create_text(400, 250, text=random_word(word_dict)[0], font=('Arial', 60, "bold"))
    canvas.delete(title)
    title = canvas.create_text(400, 125, text="Italian", font=("Ariel", 40, "italic"))


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_front_img)

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

next_card()
# ------------------------------ Code Above This ------------------------------ #
window.mainloop()