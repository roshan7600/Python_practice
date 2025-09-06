from abc import ABC , abstractmethod
class vechile():
    @abstractmethod
    def start(self):
        pass
class car(vechile):
    def start(self):
        print('car start with a key')    
class bike(vechile):
    def start(self):
        print('bike start with a button')          

obj1=car()
obj1.start()

obj2=bike()
obj2.start()