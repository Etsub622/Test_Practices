class ShoppingCart:
    def __init__(self):
        self.Cart=[]

    def addProduct(self,product):
        self.Cart.append(product)

    def getCart(self):
        total=0
        for item in self.Cart:
            total+=item.calculateTotal()
            return total         