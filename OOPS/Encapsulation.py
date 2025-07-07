# class sample():
#     def __init__(self):
#         self.__var=10
#     def getter(self):
#         return self.__var    
#     def setter(self):
#         self.__var=50
# obj=sample()            
# print(obj.getter())
# obj.setter()
# print(obj.getter())


class ATM:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    def deposit(self,amount):
        if amount>100:
            self.__balance+=amount
        else:
            print('more than 100 rupess')
    def withdraw(self,amount):
        if 100<amount<=self.__balance:
            self.__balance-=amount
        else:
            print('not possible')            
    def get_balance(self):
        return self.__balance
obj=ATM('Roshan',5000)
print(obj.get_balance())          
obj.deposit(4000)  

print(obj.get_balance())   

