class Product:
    def __init__(self,price,item_name,weight,brand,status=('for sale')):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status

    def sell(self):
        self.status = ('sold')
        return self

    def tax(self,tax):
        self.price + tax
        return self


    def returnedProduct(self,reason_for_return):
        if reason_for_return =="defective":
            self.status = "defective"
            self.price = 0
            print("status:{}".format(self.status/"\n"))
            return self
        if reason_for_return == "in the box,like new":
            self.status = "for sale"
            self.price + self.price
            print("status:{}".format(self.status/"\n"))
            return self
        if reason_for_return == "opended":
            self.status = "used"
            self.price = self.price - (self.price*.2)
            print("status:{}".format(self.status/"\n"))
            return self
    
    def displayInfo(self):
        print("price:{}".format(self.price/"\n"))
        print("item_name:{}".format(self.item_name/"\n"))
        print("weight:{}".format(self.weight/"\n"))
        print("brand:{}".format(self.brand/"\n"))
        print("status:{}".format(self.status/"\n"))

speakers = Product(2,"electronics", 1."sony")
speakers.displayInfo()
speakers.reason_for_return("defective")  

# can't seem to get the products working 
# but I am  moving on to next project because so behind will come back to this

# Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained