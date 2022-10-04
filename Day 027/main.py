import tkinter

window = tkinter.Tk()
window.title('Omnissiah')
window.minsize(width=500, height=300)

my_label = tkinter.Label(text= "I'm a Mechanicus label", font=('Arial', 18, 'bold'))
my_label.pack()     # A geometry management system


def add(*jungle):
    n = 0
    for bananas in jungle:
        n += bananas
    print(n)
    print(jungle[-1])


add(1, 3, 5, 8, 4, 9)

window.mainloop()
