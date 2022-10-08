from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
ORANGE = "#FFD8A9"
WHITE = "#FFF7E9"
CYAN = "#5F9DF7"
BLUE = "#1746A2"
GREEN = "#38E54D"
RED = "#D2001A"
YELLOW = "#FFDE00"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
my_timer = None
check_mark = ""

# ---------------------------- TIMER RESET ------------------------------- #


def time_reset():
    global check_mark
    global reps
    window.after_cancel(my_timer)
    check_mark = ''
    reps = 0
    timer_label.config(text='Timer', fg=CYAN)
    check_label.config(text=check_mark)
    canvas.itemconfig(count_down_text, text='00:00')

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global check_mark

    reps += 1

    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps % 2 != 0:
        timer_label.config(text='Work', fg=GREEN)
        countdown(work_sec)

        check_mark = f"{check_mark}✓"
    elif reps % 8 == 0:
        timer_label.config(text='Break', fg=RED)
        countdown(long_break_sec)
        check_label.config(text=check_mark)

    else:
        timer_label.config(text='Break', fg=CYAN)
        countdown(short_break_sec)
        check_label.config(text=check_mark)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    global my_timer
    count_minutes = math.floor(count / 60)
    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(count_down_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        my_timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=45, pady=20, bg=ORANGE)

timer_label = Label(padx=5, pady=5)
timer_label.config(text='Timer', bg=ORANGE, fg=CYAN, font=(FONT_NAME, 30, 'bold'))
timer_label.grid(column=1, row=0)

check_label = Label(padx=5, pady=5)
check_label.config(text=check_mark, bg=ORANGE, fg=CYAN, font=(FONT_NAME, 30, 'bold'))
check_label.grid(column=1, row=3)

canvas = Canvas(width=250, height=250, bg=ORANGE, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(125, 125, image=tomato)
count_down_text = canvas.create_text(130, 150, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button()
start_button.config(text='Start', fg=WHITE, bg=BLUE, font=(FONT_NAME, 12, 'bold'), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button()
reset_button.config(text='Reset', fg=WHITE, bg=BLUE, font=(FONT_NAME, 12, 'bold'), command=time_reset)
reset_button.grid(column=2, row=2)

window.mainloop()
