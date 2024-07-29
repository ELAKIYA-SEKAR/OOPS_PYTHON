class Geometry:

    def area(self, radius):
        return 3.14*radius*radius

    def area(self, l, b):
        return l*b


obj = Geometry()
print(obj.area(4))
# TypeError: Geometry.area() missing 1 required positional argument: 'b'
print(obj.area(4, 5))
# 20