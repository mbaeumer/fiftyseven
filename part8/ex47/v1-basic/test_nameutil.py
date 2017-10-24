import unittest
from nameutil import handle_name
from astronaut import Astronaut

class NameUtilTest(unittest.TestCase):
    def test_handle_single_lastname(self):
        name = "Martin Bäumer"
        expected_astronaut = Astronaut("Martin", "Bäumer", None)
        actual_astronaut = handle_name(name)
        self.assertTrue(actual_astronaut.firstname == expected_astronaut.firstname)
        self.assertTrue(actual_astronaut.lastname == expected_astronaut.lastname)

    def test_handle_multiple_last_name(self):
        expected_parts = []
        name = "Martin van Bäumer"
        expected_astronaut = Astronaut("Martin", "van Bäumer", None)
        actual_astronaut = handle_name(name)
        print(actual_astronaut.lastname)
        self.assertTrue(actual_astronaut.firstname == expected_astronaut.firstname)
        self.assertTrue(actual_astronaut.lastname == expected_astronaut.lastname)

if __name__ == '__main__':
    unittest.main()



