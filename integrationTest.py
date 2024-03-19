import unittest
from shopingCart import ShoppingCart
class TestShopping(unittest.TestCase):
    def testGetCartEmpty(self):
        Cart=ShoppingCart()
        total=Cart.getCart()
        self.assertEqual(total,0.0)

    def testGetCartProduct(self):
        Cart=ShoppingCart()
        Cart.addProduct(Product('a',20.0,2))
        Cart.addProduct(Product('ab',30.0,1))
        total=Cart.getCart()
        self.assertEqual(total,70.0)

unittest.main()        


