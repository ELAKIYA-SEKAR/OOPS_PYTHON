# method overloading- behaviour of method changes with the inputs


"""class Geometry:

    def area(self, radius):
        return 3.14*radius*radius

    def area(self, l, b):
        return l*b


obj = Geometry()
print(obj.area(4))
# TypeError: Geometry.area() missing 1 required positional argument: 'b'
print(obj.area(4, 5))
# 20"""
"pOSSIBLE IN JAVA BUT NOT PYTHON"
"BUT TECHNICALLY WE CAN DO IT LIKE THIS"


class Geometry:

    def area(self, a, b=0):
        if b == 0:
            print("circle", 3.14*a*a)

        else:
            print("Rectange", a*b)


obj = Geometry()
obj.area(4)
# TypeError: Geometry.area() missing 1 required positional argument: 'b'
obj.area(4, 5)
