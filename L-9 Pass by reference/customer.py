class Customer:
    def __init__(self, name, gender) -> None:
        self.name = name
        self.gender = gender


def greet(customer):
    if customer.gender == 'Male':
        print("Greetings", customer.name, "Sir")
    else:
        print("Greetings", customer.name, "Mam")

    cust2 = Customer("Praveen", "Male")
    return cust2


cust = Customer("Elakiya", "Female")
new_cust = greet(cust)
print(new_cust.name)
