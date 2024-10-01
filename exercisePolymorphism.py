#1.VEHICLE
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption
    @abstractmethod
    def drive(self, distance):
        pass
    @abstractmethod
    def refuel(self, fuel):
        pass
class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption+ 0.9)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed
            print(f'car has been drive {distance} km')
        else: 
            print ('not enough fuel')
    def refuel(self, fuel):
        self.fuel_quantity += fuel
class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__ (fuel_quantity, fuel_consumption)
    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + 1.6)
        if fuel_needed <= self.fuel_quantity:
            self.fuel_quantity -= fuel_needed
            print(f'truck has been drive {distance} km')
        else:
            print('not enough fuel')
    def refuel(self, fuel):
        self.fuel_quantity += fuel*0.95

c = Car(20,5)
c.drive(3)
print(f'car fuel quantity: {c.fuel_quantity: .2f}')
c.refuel(10)
print(f'car fuel quantity: {c.fuel_quantity: .2f}')

t=Truck(100, 15)
t.drive(5)
print(f' truck fuel quantity: {t.fuel_quantity: .2f}')
t.refuel(50)
print(f' truck fuel quantity: {t.fuel_quantity: .2f}')
t.drive(10)
print(f'truck fuel quantity: {t.fuel_quantity: .2f}')

#2.GROUPS
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
class Group:
    def __init__(self, name, people):
        self.name = n
    
        

