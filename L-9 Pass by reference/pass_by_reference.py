class Customer:
    def __init__(self, name) -> None:
        self.name = name


def greet(customer):
    print(id(customer))
    customer.name = "Praveen"
    print(customer.name)
    print(id(customer))


cust = Customer("Elakiya")
print(id(cust))

greet(cust)
print(cust.name)

