from Examen2 import MiClase
import unittest


class TestExamen(unittest.TestCase): 
    def test_ObtieneValencia (self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])    
        self.assertEqual(objeto.ObtieneValencia(1234567), 4)  
        self.assertEqual(objeto.ObtieneValencia(111), 3)    
    def test_DivisibleTempo(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])    
        self.assertEqual(objeto.DivisibleTempo(10), [1, 2, 5, 10])  
        self.assertEqual(objeto.DivisibleTempo(7), [1, 7])
    def test_ObtieneMasBailable(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.ObtieneMasBailable([0.8, 0.9, 0.7]), 0.9)  
        self.assertEqual(objeto.ObtieneMasBailable([0.3, 0.1, 0.6]), 0.6)
    def test_VerificaListaCanciones(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"]), True)  
        self.assertEqual(objeto.VerificaListaCanciones([None]), False ) 
    def test_Encuentra(self):
        objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
        self.assertEqual(objeto.Encuentra([1, 2, 3], 2), True)  
        self.assertEqual(objeto.Encuentra([10, 8 ,2], 9), False ) 
        
if __name__ == "__main__":
    unittest.main()