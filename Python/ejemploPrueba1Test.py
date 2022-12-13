import unittest
from ejemploPrueba1 import sumar5

class tests_sumar5(unittest.TestCase):
    def test_sumarar5(self):
        self.assertEqual(sumar5(1),6)
        self.assertEqual(sumar5(5),11)
        self.assertEqual(sumar5(10.102645),15.102645)
if __name__ == '__main__':
    unittest.main()
