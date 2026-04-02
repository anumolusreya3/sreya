class ATM:
    def __init__(self, name, balance, pin):
        self.name = name
        self.__balance = balance
        self.__pin = pin
    def login(self):
        entered_pin = int(input("Enter PIN: "))
        if entered_pin == self.__pin:
            print("Login Successful")
            return True
        else:
            print("Wrong PIN")
            return False
    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.__balance += amount
        print("Deposited:", amount)

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")
    def check_balance(self):
        print("Current Balance:", self.__balance)
    def menu(self):
        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                self.check_balance()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.withdraw()
            elif choice == 4:
                print("Thank you!")
                break
            else:
                print("Invalid choice")
                user = ATM("Sreya", 1000, 1234)
user = ATM("Sreya", 1000, 1234)

if user.login():
    user.menu()
