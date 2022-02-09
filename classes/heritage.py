class Animal():
    def __init__(self):
        print("Animal criado!")

    def identification(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self): #constructor of dog
        Animal.__init__(self) #constructor of animal
        print("Objeto Cachorro criado")

    def identification(self):
        print("Cachorro")

    def bark(self):
        print("Woof!")

kiara = Dog()

kiara.identification()
kiara.eat()
kiara.bark()
