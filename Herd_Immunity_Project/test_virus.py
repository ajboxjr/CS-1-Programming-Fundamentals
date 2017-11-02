import unittest
from virus import *

class test_virus(unittest.TestCase):
    
    def setUp(self):
        self.virus = Virus('Ebola', .10, 3)
        self.virus2 = Virus('Malaria', .05, 3)

    def test_get_name(self):
    	self.assertEqual(self.virus.get_name(),'Ebola')
    	self.assertEqual(self.virus2.get_name(), 'Malaria')

    def test_get_sickness_percentage(self):
    	self.assertEqual(self.virus.get_sickness_percentage(),.10)
    	self.assertEqual(self.virus2.get_sickness_percentage(), .05)
    def test_get_reproduction_rate(self):
    	self.assertEqual(self.virus.get_reproduction_rate(), 3)
    	self.assertEqual(self.virus2.get_reproduction_rate(), 3)




if __name__ == '__main__':
    unittest.main()
