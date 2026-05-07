class Car:
    def __init__(self, brand, color, year=2000):
        self.brand = brand
        self.color = color 
        #year = year
        print(f"My car color {self.color} and brand is {self.brand}")

car1 = Car("Toyota", "Red", 2000)
car2 = Car("Honda", "Black", 2003)
print(car2.brand)
print(car1.color)