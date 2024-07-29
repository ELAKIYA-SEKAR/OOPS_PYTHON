"""# single level
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand  # private member
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):
    pass


s = SmartPhone(2000, 'apple', 13)
print(s.buy())

# mutilevel


class Product:
    def review(self):
        print("Product sustomer Review")


class Phone(Product):
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand  # private member
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):
    pass


s = SmartPhone(2000, 'apple', 13)
p = Phone(30000, 'sam', 2)
s.buy()
p.review()"""

# heirarchical

# multiple


class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand  # private member
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class Product:
    def review(self):
        print("Product sustomer Review")


class SmartPhone(Phone, Product):
    pass


s = SmartPhone(2000, 'apple', 13)
s.buy()
s.review()


# method resolution order - class methods which frst gets inherits executes first


class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.__brand = brand  # private member
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class Product:
    def review(self):
        print("Product sustomer Review")

    def buy(self):
        print("Buying a Product")


class SmartPhone(Phone, Product):  # phone's buy coems as first
    # class SmartPhone(Product, Phone): #Product's buy coems as first

    pass


s = SmartPhone(2000, 'apple', 13)
s.buy()
