from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="card_front.png")

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)


# ------------------------------ Code Above This ------------------------------ #
window.mainloop()