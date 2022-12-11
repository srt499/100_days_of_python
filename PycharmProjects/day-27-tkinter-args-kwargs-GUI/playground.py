# to allow unlimited arguments for a function, use *args
def add(*args):
    print(args[1])
    total = 0
    for n in args:
        total += n
    print(total)


add(5, 10, 20, 30, 40)


# Unlimited key-word arguments, kwargs is a dictionary
def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs['add'])
    print(kwargs['multiply'])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get('color')
        self.seats = kw.get("seats")


my_car = Car(make= "Nissan", model="Skyline")

print(my_car.make, my_car.model)