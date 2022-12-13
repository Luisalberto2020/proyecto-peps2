import unittest
from ejemploPrueba3 import es_primo

class numero_primo(unittest.TestCase):
    def test_numero_primo(self):
        self.assertTrue(es_primo(7))
        self.assertTrue(es_primo(3))
        self.assertFalse(es_primo(8))
if __name__ == '__main__':
    print("hola")
    unittest.main()