class Atm:
  def __init__(self):
    self.pin = 0
    self.balance = 0
    self.menu()

  

  def check(self):
    self.crosscheck = int(input("Enter your PIN"))
    if self.crosscheck == self.pin:
      return 1
    else:
      return 0

  def check_and_creat_pin(self):
    self.temp = int(input("Enter Your Old PIN, If First Time Enter 0"))
    if self.temp == self.pin:
      self.pin = int(input("Enter new PIN"))
      return 1
    else:
      return 0
   
  def deposit(self):
    temp = self.check()
    if temp == 1:
      self.balance += int(input("Enter Amount"))
      print("Available Balance ",self.balance)
      self.menu()
    else:
      print("Invalid PIN")

  def check_balance(self):
    temp = self.check()
    if temp == 1:
      print(self.balance)
      self.menu()
  def withdraw(self):
    temp = self.check()
    if temp == 1:
      temp = int(input("Enter the Amount to withdraw"))
      if temp <= self.balance:
        self.balance -= temp
        print("Available Balance ",self.balance)
        self.menu()
    else:
      print("invalid PIN")
      
    



  
  def menu(self):
    temp = int(input("""
                   Press 1 For Creat Pin.
                   Press 2 For Deposit.
                   Press 3 For Check Balance.
                   Press 4 For Withdraw.
                   Press Any Key to Exit.
    """))
    
    if temp == 1:
      print("### Processing to Creat Your Pin ###")
      self.creat_pin()
    elif temp == 2:
      print("### Processing to Deposit ###")
      self.deposit()
    elif temp == 3:
      print("### Processing to Check Balance ###")
      self.check_balance()
    elif temp == 4:
      print("### Processing to Withdraw ###")
      self.withdraw()
    elif temp == 5:
      print("EXITING NOW.....")
    else:
      print("### Invalid Entry ###")
  def creat_pin(self):
    temp = self.check_and_creat_pin()
    if temp == 1:
      print("PIN Change Succesfully")
      self.menu()
    else:
      print("Wrong old PIN")
    

sbi = Atm()
