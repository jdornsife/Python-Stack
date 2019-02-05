class Car:
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.display_all()
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12 

    def display_all(self):
        print("price:{},speed:{},fuel:{},mileage:{},tax:{}".format(self.price,self.speed,self.fuel,self.mileage,self.tax))
       
         
mustang = Car(5000,120,'full',15)
bmw =  Car(25000,180,'full',15)
lexus = Car(30000,120,'empty',20)
jetta = Car(15000,120,'full',20)
passat = Car(5000,120,'full',20)
tundra = Car(5000,120,'full',89)






