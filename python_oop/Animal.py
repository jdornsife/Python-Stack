class Animal:
    def __init__(self,given_name,given_health):
        self.name = given_name
        self.health = given_health

    def walk(self):
        self.health -=1

    def run(self):
        self.health -=5

    def display_health(self):
        print("health is:{}".format(self.health))

sparkie = Animal("sparkie",100)
sparkie.walk(3)
sparkie.run(2)
sparkie.display_health

class Dog(Animal):
    def __init__(self,given_name):
        super().__init__(given_name,150)   
        
    def pet(self):
        self.health +=5

    def display_health(self):
        # super().(display_health)
        print("Dog Health:{}".format(self.health))
    

Dog = Dog("lady")
lady.walk(3)
lady.run(2)
lady.pet(1)
lady.display_health()

class Dragon(Animal):
    def __init__(self,given_name):
        
    def fly(self):
        self.health -=10

    def display_health(self):
        # super().(display_health)
        print("I'm a Dragon{}".format(self.health))
        

Dragon = Dragon("toothless")
toothless.walk(1)
toothless.run(1)
toothless.fly(2)
toothless.display_health()


            