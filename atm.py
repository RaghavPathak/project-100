import random
number = random.randint(1000,10000)
class atm(object):
    def __init__(self,cardNumber,pinNumber,amount):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
        self.amount=amount
   
    def moneyWidrawl(self):
        print(self.amount + "has been widrawl from your account")

    def balance(self):
        print("Your account balance is" + number)

person1 = atm("123456","654321","1000")
print(person1.balance())

