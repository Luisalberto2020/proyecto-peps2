import unittest
from ejemploPrueba3 import recuperar_numeros_primos

class numero_primo(unittest.TestCase):
    def test_numero_primo(self):
        self.assertTrue(recuperar_numeros_primos(7))
        self.assertTrue(recuperar_numeros_primos(3))
        self.assertFalse(recuperar_numeros_primos(8))
if __name__ == '__main__':
    print("hola")
    unittest.main()