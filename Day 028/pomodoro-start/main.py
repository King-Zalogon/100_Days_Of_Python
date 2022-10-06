from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
ORANGE = "#FFD8A9"
WHITE = "#FFF7E9"
CYAN = "#5F9DF7"
BLUE = "#1746A2"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=45, pady=20, bg=ORANGE)

timer_label = Label(padx=5, pady=5)
timer_label.config(text='Timer', bg=ORANGE, fg=CYAN, font=(FONT_NAME, 30, 'bold'))
timer_label.grid(column=1, row=0)

check_mark = '✓'
check_label = Label(padx=5, pady=5)
check_label.config(text=check_mark, bg=ORANGE, fg=CYAN, font=(FONT_NAME, 30, 'bold'))
check_label.grid(column=1, row=3)

canvas = Canvas(width= 250, height= 250, bg=ORANGE, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(125, 125, image=tomato)
canvas.create_text(130, 150, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button()
start_button.config(text='Start', fg=WHITE, bg=BLUE, font=(FONT_NAME, 12, 'bold'))
start_button.grid(column=0, row=2)

reset_button = Button()
reset_button.config(text='Reset', fg=WHITE, bg=BLUE, font=(FONT_NAME, 12, 'bold'))
reset_button.grid(column=2, row=2)



window.mainloop()