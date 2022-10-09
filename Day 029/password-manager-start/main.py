from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(pady=20, padx=20)

canvas = Canvas(width=200, height=200)
logo_img= PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.pack()

# End of code
window.mainloop()
