import unittest

def additionner(a,b):
    return a+b


class TestUnitaireDemo(unittest.TestCase):
    def setUp(self):
        print("setUp")
    
    def tearDown(self):
        print("tearDown")
        
    def test_additionner1(self):
        print("test_additionner1")
        self.assertEqual(additionner(5,10), 15)

    def test_additionner2(self):
        print("test_additionner2")
        self.assertEqual(additionner(6,10), 16)


unittest.main()


