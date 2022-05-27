class Account:
    Account="prime"
    def __init__(self,name,phone_number,account_number,id,balance):
        self.name=name
        self.phone_number=phone_number
        self.account_number=account_number
        self.id=id
        self.balance=balance
    
    def withdraw (self,amount):
        self.amount=amount
        self.balance -=self.amount
        return f"Thank you for the withdraw, your new balance is  {self.balance}"
    
    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        return f"Thankyou for depositing ,your new balance is  {self.balance}"
    
        
