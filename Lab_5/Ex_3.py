class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_efficiency):
        super().__init__(make, model, year)
        self.fuel_efficiency = fuel_efficiency

    def calculate_mileage(self, distance):
        return distance / self.fuel_efficiency

class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        super().__init__(make, model, year)
        self.towing_capacity = towing_capacity
    def calculate_towing_capacity(self):
        return f"Towing Capacity: {self.towing_capacity}"

car = Car(make="Toyota", model="Corolla", year=2022, fuel_efficiency=30)
print(car.display_info())
print(f"Mileage : {car.calculate_mileage(150)} miles")
motorcycle = Motorcycle(make="Yamaha", model="R1M", year=2024)
print(motorcycle.display_info())
truck = Truck(make="Ford", model="F-150", year=2023, towing_capacity=8000)
print(truck.display_info())
print(truck.calculate_towing_capacity())
