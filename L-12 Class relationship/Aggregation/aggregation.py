class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_pincode, new_state):
        self.name = new_name
        self.address.change_address(new_city, new_state, new_pincode)


class Address:
    def __init__(self, city, state, pincode) -> None:
        self.city = city
        self.state = state
        self.pincode = pincode

    def change_address(self, new_city, new_state, new_pincode):
        self.city = new_city
        self.state = new_state
        self.pincode = new_pincode


address1 = Address('coimbatore', 'TN', 641108)

customer1 = Customer('Elaki', 'F', address1)
customer1.edit_profile("sekar", "chennai", "kolk", 453)
print(customer1.address.city)
print(customer1.address.pincode)
print(customer1.name)
