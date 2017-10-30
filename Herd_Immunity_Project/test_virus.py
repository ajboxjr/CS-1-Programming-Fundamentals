import unittest
from virus import *

class test_virus(unittest.TestCase):
    
    def setUp(self):
        self.virus = Virus('Ebola', .10, 3)
        self.virus2 = Virus('Malaria', '.05', 3)

    def test_get_name(self):
    	self.assertEqual(self.virus.get_name(),'Ebola')

    def test_get_sickness_percentage(self):
    	self.assertEqual(self.virus.get_sickness_percentage(),.10)




if __name__ == '__main__':
    unittest.main()
