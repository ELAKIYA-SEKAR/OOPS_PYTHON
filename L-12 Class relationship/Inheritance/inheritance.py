class User:

    def login(self):
        print("login")

    def register(self):
        print("Register")


class Student(User):

    def enroll(self):
        print("Enroll")

    def enroll(self):
        print("Review")




stu1 = Student()

stu1.register()
stu1.enroll()
stu1.login()


tu1 = User()

tu1.register()
tu1.enroll()
tu1.login()
