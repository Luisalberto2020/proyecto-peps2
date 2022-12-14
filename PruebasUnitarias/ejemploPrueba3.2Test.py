import unittest
from ejemploPrueba3 import recuperar_numeros_primos

class numero_primo2(unittest.TestCase):
    def test_numero_primo2(self):
        self.assertNotEqual(recuperar_numeros_primos(3), [2, 3, 5, 7] )
        self.assertEqual(recuperar_numeros_primos(11),[2, 3, 5, 7, 11] )
        self.assertEqual(recuperar_numeros_primos(27), [2, 3, 5, 7, 11, 13, 17, 19, 23] )

if __name__ == '__main__':
    unittest.main()