class A:
    def m1(self):
        return 20


class B(A):
    def m1(self):
        val = super().m1()+30
        return val


class C(B):
    def m1(self):
        val = self.m1()+30
        return val


obj = C()
print(obj.m1())

# RecursionError: maximum recursion depth exceeded
# self is nothing but object itself so it repeats on and on
