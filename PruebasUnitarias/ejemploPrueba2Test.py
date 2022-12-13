import unittest
from ejemploPrueba2 import *
from datosPrueba2 import *

class ejemploPrueba2Test(unittest.TestCase):
    def test_busquedaEncontrada (self):
        self.assertTrue([]!=jsonBuscar("prioridad",datosCompra))
    def test_busquedaNoEncontrada (self):
        self.assertTrue([]==jsonBuscar("otracosa",datosCompra))
    def test_is_a_list(self):
        self.assertIsInstance (jsonBuscar("opciones", datosCompra), list)
if __name__ == '__main__':
    unittest.main()
