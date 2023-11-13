import unittest
from Examen2 import MiClase

class MyTestCase(unittest.TestCase):
    def test_ObtieneValencia(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.ObtieneValencia(111111), 6)  # add assertion here

    def test_ObtieneValencia2(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.ObtieneValencia(157823), 4)  # add assertion here

    def test_DivisibleTempo(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.DivisibleTempo(4),[1,2,4])  # add assertion here

    def test_DivisibleTempo2(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.DivisibleTempo(36), [1,2,3,4,6,9,12,18,36])  # add assertion here


if __name__ == '__main__':
    unittest.main()
