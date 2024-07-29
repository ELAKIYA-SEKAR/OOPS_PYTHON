# example 1
class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num


class Child(Parent):
    def show(self):
        print("this is in child class")


son = Child(100)

print(son.get_num())

son.show()

# Example 2


class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num


class Child(Parent):

    def __init__(self, val, num):
        self.__val = val

    def get_val(self):
        return self.__val


son = Child(100, 10)

# when a child constructor wont invoke the parent constructor
print("parent", son.get_num())
# but parent constructor invoke child constructor
print("child", son.get_val())

# example 3
