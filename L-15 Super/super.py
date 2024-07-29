"""# example 1
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand  # private member
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):
    def buy(self):
        print("Buying a Smartphone")
        super().buy()  # calls the parent's method


s = SmartPhone(2000, 'apple', 13)
print(s.buy())"""
# s.super().buy()  # error
# super cant be used outside the class
# super can access parents method and parents constructor we cant use for attributes


# example 2
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand  # private member
        self.camera = camera


class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        print("first thiss")
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside smartphone constructor")


s = SmartPhone(2000, 'apple', 13, "ios", 2)
print(s.__price)  # error
print(s.brand)
