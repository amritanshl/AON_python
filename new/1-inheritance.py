class Car: # BASE CLASS (Parent)
    def __init__(self, brand , model):
        self.brand = brand
        self.model= model

    def horn(self):
        print(f"The {self.brand} says: Beep Beep!")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def charge(self):
        print(f"The {self.brand} is charging its {self.battery_size}kWh battery.")

basic_car = Car("Toyota", "Corolla")
basic_car.horn()

my_tesla = ElectricCar("Tesla", "Model S", 90)
my_tesla.horn()
my_tesla.charge()