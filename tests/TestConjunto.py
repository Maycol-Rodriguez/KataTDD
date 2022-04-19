import unittest
from src.Logica.Conjunto import Conjunto

class MyTestCase(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])
        self.assertEqual(conjunto.promedio())


if __name__ == '__main__':
    unittest.main()
