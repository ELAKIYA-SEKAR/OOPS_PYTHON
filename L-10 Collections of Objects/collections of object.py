# collection of object is the collection of objects
# in the form of lists, dictionaries

class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print("I am", self.name)


c1 = Customer('Elakiya', 20)
c2 = Customer('Sekar', 50)
c3 = Customer('Eswari', 47)

L = [c1, c2, c3]
# for i in L:
#   print(i)
# for i in L:
#   print(i.name, i.age)
for i in L:
    i.intro()
# print(i.intro()) --> i.intro() prints the intro. printing the i.intro() result none as it doesnt return any value
