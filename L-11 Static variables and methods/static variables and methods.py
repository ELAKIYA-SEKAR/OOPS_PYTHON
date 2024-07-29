class Atm:
    # static or class variable
    __counter = 1

    def __init__(self):
        # instance variable
        self.pin = ""
        self.balance = 0
        # static variable is defined
        self.sno = Atm.__counter
        Atm.__counter += 1

        self.menu()

    @staticmethod
    def get_counter():
        # as we dont use the object here, we shouldnt specify self
        # it expects object name in which we have given class name
        # in static method we dont give self as there is no need
        return Atm.__counter

    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("It is not possible")

    def menu(self):
        user_input = input("""
Hello,how would you like to proceed?
1.Enter 1 to create pin
2. Enter 2 to deposit
3. Enter 3 to withdraw
4. Enter 4 to check balance
5. Enter 5 to exit""")
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("Thank you.Come Again")
        else:
            print("You have entered wrong number.Thank you")

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin set succesfully.")

    def deposit(self):
        attempts = 0
        while attempts < 3:
            temp = input("Enter your Account pin: ")
            if temp == self.pin:
                deposit_amount = int(
                    input("Enter the amount you want to deposit: "))
                self.balance += deposit_amount
                print("Amount is deposited succesfully.")
                return
            else:
                attempts += 1
                print(f"Incorrect pin. You have {
                      3-attempts} attempts remaining")
        print("Too many incorrect attempts.Try again later")

    def withdraw(self):
        attempts = 0
        while attempts < 3:
            temp = input("Enter your Account pin: ")
            if temp == self.pin:
                deposit_amount = int(
                    input("Enter the amount you want to Withdraw: "))
                if deposit_amount > self.balance:
                    print("Insufficient balance")
                else:
                    self.balance -= deposit_amount
                    print("Amount is Withdrawn succesfully.")
                    return
            else:
                attempts += 1
                print(f"Incorrect pin. You have {
                    3-attempts} attempts remaining")
                print("Too many incorrect attempts.Try again later")

    def check_balance(self):
        attempts = 0
        temp = input("Enter your Account pin: ")
        if temp == self.pin:
            print("You current balance is", self.balance)
        else:
            attempts += 1
            print(f"Incorrect pin. You have {
                3-attempts} attempts remaining")
            print("Too many incorrect attempts.Try again later")
