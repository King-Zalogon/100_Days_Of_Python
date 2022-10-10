from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_gen():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #


def pass_save():
    site = site_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    with open('data.txt', mode='a') as file:
        file.write(f"\n{site} | {user} | {password}")
    site_entry.insert(0, "")
    user_entry.insert(0, "some_mail_address@gmail.com")
    pass_entry.insert(0, " ")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(pady=50, padx=50)

site_label = Label(text='Website:')
site_label.grid(column=0, row=1)
site_label.config(padx=5, pady=5)

user_label = Label(text='Email/Username:')
user_label.grid(column=0, row=2)
user_label.config(padx=5, pady=5)

pass_label = Label(text='Password:')
pass_label.grid(column=0, row=3)
pass_label.config(padx=5, pady=5)

site_entry = Entry(width=35)
site_entry.grid(column=1, row=1, columnspan=2)
site_entry.focus()


user_entry = Entry(width=35)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "some_mail_address@gmail.com")


pass_entry = Entry(width=17)
pass_entry.grid(column=1, row=3)


generate_button = Button(text='Generate Password', command=pass_gen)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=35, command=pass_save)
add_button.grid(column=1, row=4, columnspan=2, pady=5)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# End of code
window.mainloop()
