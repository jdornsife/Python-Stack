class Bike:
   def  __init__(self,price,max_speed,miles=0):
       self.price = price
       self.max_speed = max_speed
       self.miles = miles
       self.display_info()


   def display_info (self):
       print("the price of the bike is: {}, it's maximum speed is: {}, and the total miles are:{},".format(self.price,self.max_speed,self.miles))
       
       
		
   def ride(self):
       self.miles += 10
       print('riding')


   def reverse(self):
       self.miles -= 5 
       print('reversing')

huffy = Bike(200,50)
schwinn = Bike(100,40,50)

# huffy.ride()
# schwinn.ride()
# huffy.ride()
# schwinn.ride()
# huffy.ride()
# schwinn.ride()

# huffy.reverse()
# schwinn.reverse()

# huffy.ride()
# swhinn.ride()
# huffy.ride()
# swhinn.ride()

# huffy.reverse()
# schwinn.reverse()
# huffy.reverse()
# schwinn.reverse()

# huffy.reverse()
# schwinn.reverse()
huffy.reverse()
schwinn.reverse()







    