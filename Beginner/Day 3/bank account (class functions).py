class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
        
    def deposit(self,amount):
      self.balance += amount
      print("The new balance is " + str(self.balance))
    
    def withdraw(self,amount):
      self.balance -= amount
      print("The new balance is " + str(self.balance))

    def display_balance(self):
      print("Your balance " + str(self.balance))

BobMarley = BankAccount("Bob", "Marley", 1234, "saving", 5678, 1000)

BobMarley.deposit(96)
BobMarley.withdraw(25)
BobMarley.display_balance()