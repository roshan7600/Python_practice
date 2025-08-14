#  POLYMORPHISM : - poly means (many) and morphism means (forms)
# Same method name behaves differently in the different class is called ploymorphism
# There are two types of 1) method overloading
#                        2) method overriding  


# python not supported directly method overloading so we can achived by a (*args ,default parameter and using reduce function)


class Animal():
    def speak(self):
        print('animal speaks')
class Dog(Animal):
    def speak(self):
        print('dog barks')    
class Cat(Animal):
    def speak(self):
        print('cat meows')        
    def make_sound(Animal)  :
        Animal.speak()      
    make_sound(Dog())
    # make_sound(Cat())    
