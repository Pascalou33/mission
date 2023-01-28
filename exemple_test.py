import unittest
from unittest.mock import patch

def additionner(a,b):
    return a+b


def conversion_nombre():
    num_str = input("Rentrer un nombre : ")
    return int(num_str)


class TestUnitaireDemo(unittest.TestCase):
    def setUp(self):
        print("setUp")
    
    def tearDown(self):
        print("tearDown")
        
    def test_additionner_nombre_positif(self):
        print("test_additionner_nombre_positif")
        self.assertEqual(additionner(5,10), 15)
        self.assertEqual(additionner(6,20), 26)
        self.assertEqual(additionner(6,-6), 0)

    def test_additionner_nombre_negatif(self):
        print("test_additionner_nombre_negatif")
        self.assertEqual(additionner(6,-10), -4)
        self.assertEqual(additionner(-6,-10), -16)
        self.assertEqual(additionner(-6,10), 4)
        
    def test_conversion_nombre_valide(self):
        print("test_conversion_nombre_valide")
        with patch("builtins.input", return_value="10"):
            self.assertEqual(conversion_nombre(), 10)
        
    def test_conversion_entree_invalide(self):
        print("test_conversion_entree_invalide")
        with patch("builtins.input", return_value="dzrg"):
            self.assertRaises(ValueError, conversion_nombre)


unittest.main()


