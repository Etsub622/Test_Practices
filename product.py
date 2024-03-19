class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def calculateTotal(self):
        val=self.price*self.quantity
        if val<0:
            raise (ValueError())
        else:
            return val    














