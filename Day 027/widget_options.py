# from tkinter import *
#
# window = Tk()
# window.title('Omnissiah')
# window.minsize(width=500, height=300)
#
# my_label = Label(text="I'm a Mechanicus label", font=('Arial', 18, 'bold'))
# my_label.pack()     # A geometry management system
# my_label['text'] = 'Hail Magus Ramirez'
# my_label.config(text='Praise the Omnissiah!')
#
#
# def add(*jungle):
#     n = 0
#     for bananas in jungle:
#         n += bananas
#     print(n)
#     print(jungle[-1])
#
#
# # add(1, 3, 5, 8, 4, 9)
#
#
# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs['add']
#     n *= kwargs['multiply']
#     print(n)
#
#
# # calculate(2, add=3, multiply=5)
#
#
# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get('make')
#         self.model = kw.get('model')
#         self.color = kw.get('color')
#         self.seats = kw.get('seats')
#
#
# # my_car = Car(make='Nissan')
# # print(my_car.make)
# # print(my_car.model)
#
# def test(*args):
#     print(args)
#
# # test(1,2,3,4)
#
# # Button
#
#
# def button_click():
#     new_text = my_input.get()
#     my_label.config(text=new_text)
#     my_label.pack()
#

# Entry
# my_input = Entry(width=20)
# my_input.pack()
# button = Button(text='Click me', command=button_click)
# button.pack()
#
# # Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# # Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
# # Buttons
#
#
# def action():
#     print("Do something")
#
#
# # calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# # Entries
# entry = Entry(width=30)
# # Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# # Gets text in entry
# print(entry.get())
# entry.pack()
#
# # Text
# text = Text(height=5, width=30)
# # Puts cursor in textbox.
# text.focus()
# # Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# # Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# # Spinbox
#
#
# def spinbox_used():
#     # gets the current value in spinbox.
#     print(spinbox.get())
#
#
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# # Scale
# # Called with current scale value.
#
#
# def scale_used(value):
#     print(value)
#
#
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# # Checkbutton
#
#
# def checkbutton_used():
#     # Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
#
#
# # variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# # Radiobutton
#
#
# def radio_used():
#     print(radio_state.get())
#
#
# # Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# # Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()