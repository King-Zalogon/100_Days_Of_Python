import tkinter as tk

THEME_COLOR = "#375362"

window = tk.Tk()
window.config(width=450, height=600, bg=THEME_COLOR, pady=10, padx=10, )
window.title('Quizzer')

label = tk.Label(text="Score")
label.config(font=('Arial', 25, "bold"), bg=THEME_COLOR, fg='#ffffff', padx=10, pady=10)
label.grid(row=0, column=1)

canvas = tk.Canvas()
canvas.config(width=50, height=50, )
canvas.grid(row=1, column=0)

t_button = tk.Button()
true_img = tk.PhotoImage(file="images/true.png")
t_button.config(image=true_img, highlightthickness=0, padx=10, pady=10)
t_button.grid(row=2, column=0)

f_button = tk.Button()
false_img = tk.PhotoImage(file="images/false.png")
f_button.config(image=false_img, highlightthickness=0, padx=10, pady=10)
f_button.grid(row=2, column=1)


# Code above
window.mainloop()
