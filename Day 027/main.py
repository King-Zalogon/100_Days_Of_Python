import tkinter

window = tkinter.Tk()
window.title('Omnissiah')
window.minsize(width=500, height=300)

my_label = tkinter.Label(text= "I'm a Mechanicus label", font=('Arial', 18, 'bold'))
my_label.pack()     # A geometry management system


window.mainloop()
