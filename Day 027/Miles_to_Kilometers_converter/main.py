from tkinter import *

window = Tk()
window.title('Miles to Km Converter')
# window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

label_a = Label(text="is equal to", font=('Arial', 12, 'bold'))
label_a.grid(column=0, row=1)

label_b = Label(text=f"{0}", font=('Arial', 12, 'bold'))
label_b.grid(column=1, row=1)

label_c = Label(text="Km", font=('Arial', 12, 'bold'))
label_c.grid(column=2, row=1)

label_d = Label(text="Miles", font=('Arial', 12, 'bold'))
label_d.grid(column=2, row=0)

entry = Entry(width=10)
entry.grid(column=1, row=0)


def convert():
    miles = int(entry.get())
    km = round((miles * 1.609), 1)
    label_b.config(text=f"{km}")


button = Button(fg="red", bg="blue", text="Calculate", command=convert)
button.grid(column=1, row=2)


window.mainloop()
