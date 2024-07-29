class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand  # private member
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")


class SmartPhone(Phone):
    def buy(self):
        print("Buying a smart phone")


s = SmartPhone(2000, 'apple', 13)
s.buy()
# which value is called
# its method over riding comes under polymorphism
"""3 in polymorphismm- method overriding,method overloading,operator overloading

"""
