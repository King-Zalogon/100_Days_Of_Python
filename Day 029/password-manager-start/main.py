
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_gen():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += (choice(letters) for _ in range(randint(8, 10)))
    password_list += (choice(symbols) for _ in range(randint(2, 4)))
    password_list += (choice(numbers) for _ in range(randint(2, 4)))

    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def pass_save():
    site = site_entry.get()
    user = user_entry.get()
    password = pass_entry.get()
    new_data = {
        site: {
            "email": user,
            "password": password,
        }
    }

    if len(site) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(title='Oops!', message="Please don't leave any field empty")

    else:
        is_ok = messagebox.askokcancel(title=site, message=f"These are the details entered:\nUser or Email: {user}"
                                                           f"\nPassword: {password}")

        if is_ok:
            try:
                with open('data.json', mode='r') as file:
                    data = json.load(file)  # Reading old data

            except FileNotFoundError:
                with open('data.json', mode='w') as file:
                    json.dump(new_data, file, indent=4)

            else:
                data.update(new_data)  # Updating old data with new data

                with open('data.json', mode='w') as file:
                    json.dump(data, file, indent=4)  # Saving updated data
                    # file.write(f"{site} | {user} | {password}\n") <-- Old code
            finally:
                site_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- SEARCH BUTTON ------------------------------- #


def pass_search():
    web = site_entry.get()

    try:
        with open('data.json', mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(f"No {file} database found")
    else:
        try:
            election = messagebox.askquestion(
                title="Search results",
                message=f"{web}\nEmail: {data[web]['email']}\nPassword: {data[web]['password']}\nDo you want to copy "
                        f"your password to the clipboard?"
            )

        except KeyError:
            messagebox.showwarning(title="Info not found", message=f"No stored details for {web}")

        else:
            if election == 'yes':
                pyperclip.copy(data[web]['password'])
            else:
                pass


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

site_entry = Entry(width=25)
site_entry.grid(column=1, row=1)
site_entry.focus()

user_entry = Entry(width=43)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "some_mail_address@gmail.com")

pass_entry = Entry(width=25)
pass_entry.grid(column=1, row=3)

search_button = Button(text='Search', width=14 , command=pass_search)
search_button.grid(column=2, row=1, pady=5)

generate_button = Button(text='Generate Password', command=pass_gen)
generate_button.grid(column=2, row=3, pady=5)

add_button = Button(text='Add', width=30, command=pass_save)
add_button.grid(column=1, row=4, columnspan=2, pady=5)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# End of code
window.mainloop()
