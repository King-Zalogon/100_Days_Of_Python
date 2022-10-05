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


# add(1, 3, 5, 8, 4, 9)


def calculate(n, **kargs):
    print(kargs)
    n += kargs['add']
    n *= kargs['multiply']
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')


my_car = Car(make='Nissan')
print(my_car.make)
print(my_car.model)

def test(*args):
    print(args)

test(1,2,3,4)

window.mainloop()
