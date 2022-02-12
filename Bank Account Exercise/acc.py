from tabnanny import check


class Account:

    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())
    
    def withdraw(self, amount,fees=0):
        self.balance = self.balance - (int(amount) + int(fees))
        self.commit()

    def deposit(self, amount):
        self.balance = self.balance + int(amount)
        self.commit()

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """This class generates checking account objects"""
    type="checking"
    def __init__(self,filepath,fees):
        Account.__init__(self,filepath)
        self.fees = fees

    def transfer(self,amount):
        self.withdraw(amount,self.fees)
        


awni_checking = Checking('awni.txt',1)


awni_checking.transfer(500)

print(awni_checking.balance)

print(awni_checking.type)

#####

medo_checking = Checking('medo.txt',1)


medo_checking.transfer(500)

print(medo_checking.balance)
 
print(medo_checking.type)


print(awni_checking.__doc__)