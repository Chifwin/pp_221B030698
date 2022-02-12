class Account:
    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.balance = balance

    def deposit(self, money: int):
        if (money < 0): 
            self.withdraw(-money)
        else:
            self.balance += money
            print(f"Now balance of {self.owner} = {self.balance}")

    def withdraw(self, money: int):
        if (money < 0): 
            self.deposit(-money)
        elif money > self.balance:
            print(f"{self.owner} have not enough money on his(her) balance: need {money}, have {self.balance}")
        else:
            self.balance -= money
            print(f"Now balance of {self.owner} = {self.balance}")

if __name__ == "__main__":
    Boris = Account("Boris", 50)
    Boris.deposit(5)
    Boris.withdraw(55)
    Vasya = Account("Vasya", 100)
    Vasya.deposit(-5)
    Vasya.deposit(-111)
    Vasya.withdraw(-10)