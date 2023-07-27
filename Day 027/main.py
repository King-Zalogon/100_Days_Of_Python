from tkinter import *

window = Tk()
window.title("I'm the title of my GUI")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

my_label = Label(text="I'm label of my GUI", font=('Arial', 18, 'bold'))
# my_label.pack(side='bottom', expand=True)  # A geometry management system
my_label.grid(column=0, row=0)     # A geometry management system


def action():
    print("Do something")


button = Button(text="Click Me", command=action)
button.grid(column=1, row=1)
button.config(pady=10, padx=10)

new_button = Button(text="Click Me 2", command=action)
new_button.grid(column=2, row=0)
# new_button.config(pady=10, padx=10)

# Entries
entry = Entry(width=20)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.grid(column=3, row=2)


window.mainloop()  # Goes at the end of my program and keeps the window running until closed
