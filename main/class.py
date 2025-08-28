
class animal :
    def __init__(self, name ):
        self.name = name
        self.is_allive = True
    
    def eat (self):
        print(f"{self.name} is eating")

    def sleep (self):
        print(f"{self.name} is asleep")

class Dog (animal):
    def speak (self):
        print(f"{self.name} woof")
 
class Cat (animal):
    def speak (self):
        print(f"{self.name} moew")

class Mouse (animal):
    pass

dog = Dog("scooby")
cat = Cat("tom")
mouse = Mouse("jerry")


print(dog.name)

cat.speak()
print(mouse.name)
print(f"{cat.name} is allive ?  {cat.is_allive}")




