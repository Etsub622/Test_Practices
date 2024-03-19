import unittest
from product import Product

class TestProduct(unittest.TestCase):
    # def testCalculateTotal(self):
    #     product=Product('product1',20.0,2)
    #     total=product.calculateTotal()
    #     self.assertEqual(total,40.0)

    def testZero(self):
        product=Product('product3',20.0,0)
        total=product.calculateTotal()
        self.assertEqual(total,0)
    # test for negative quantities
    def testNegative(self):
        product2=Product('shoe',5.0,-2)
        with self.assertRaises(ValueError):
            total=product2.calculateTotal()

unittest.main()            



    




