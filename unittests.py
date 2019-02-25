import unittest
from pymongo import MongoClient

from MongoDB import Film, Actor

class TestFilmMethods(unittest.TestCase):

    def test_get_nb_films(self):
        self.assertEqual(Film.get_nb_films(db), 0)

if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    db = client.unittest_pymongo

    unittest.main()

    client.close()
