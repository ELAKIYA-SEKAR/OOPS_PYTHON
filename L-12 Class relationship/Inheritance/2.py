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


class FeaturePhone(Phone):
    pass


class SmartPhone(Phone):
    pass


s = SmartPhone(2000, 'apple', 13)
print(s.price)
print(s.__brand)
# child cant access the parents private attributes
"""Traceback (most recent call last):
  File "c:\Users\ELAKIYA SEKAR\Documents\OOPS\OOPS_PYTHON\L-12 Class relationship\Inheritance\2.py", line 25, in <module>       
    print(s.__brand)
          ^^^^^^^^^
AttributeError: 'SmartPhone' object has no attribute '__brand'  """
