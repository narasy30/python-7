
class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display(self):
        print(f"Brand: {self.brand}, Speed: {self.speed} km/h")

def create_car():
    car1 = Car("Toyota", 180)
    return car1

my_car = create_car()
my_car.display()


