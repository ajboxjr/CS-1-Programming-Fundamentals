import unittest
import person
import virus

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person1 = person.Person(1,False, infected=virus.Virus('Ebola', .3, .6))
        self.person2 = person.Person(2,True)

    def tearDown(self):
        pass
        
    def test_did_survive_infection(self):
        self.assertEqual(self.person1.did_survive_infection(), False)
        self.assertEqual(self.person2.did_survive_infection(), True)


if __name__ == '__main__':
    unittest.main()
