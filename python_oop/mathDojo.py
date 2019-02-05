class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, *args):
        self.adding = 0
        
        for value in args:
            self.adding += value
            self.result += self.adding 
        return self

    def subtract(self, *args):
        self.subtract = 0

        for value in args:
            self.subtract += value
            self.result -= self.subtract
        return self

    MathDojo = MathDojo
    MathDojo.add(2)
    MathDojo.add(5)
    MathDojo.subtract(2)
    MathDojo.result
    print(MathDojo)

class Md:
    def __init__(self):
        self.result = 0

    def add(slef, *args):
        for object in args:
            if type(object) == list:
                for value in object:
                    self.result += value
            elif type (object) == int:
                self.result += object
            return self

    def subtract(self, *args):
        for object in args:
            if type(object) == list:
                for value in object:
                    self.result -= value
            elif type (object)== int:
                    self.result -= object
        return self

    x = Md
    .add(2)
    .add(2,5,1)
    Md.subtract(3,2)
    x.result
    print(x)
                    
