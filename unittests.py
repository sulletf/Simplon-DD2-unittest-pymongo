import unittest
from pymongo import MongoClient

from MongoDB import Film, Actor

class TestFilmMethods(unittest.TestCase):

    def test_get_nb_films(self):
        self.assertEqual(Film.get_nb_films(db), 450)

    def test_get_actors(self):
        film = Film('tt6674514')
        actors_list = film.get_actors(db)
        self.assertEqual(':'.join(actors_list), ' Kangaroo Dundee\n: Terri Irwin\n: Phil Wollen\n: Tim Flannery\n: Peter Singer\n')

class TestActorMethods(unittest.TestCase):

    def test_constructor(self):
        actor = Actor('Nicolas Zanforlini')
        self.assertIsInstance(actor, Actor)
        self.assertEqual(actor.name, 'Nicolas Zanforlini')
        self.assertIsInstance(actor.films, list)
        self.assertEqual(len(actor.films), 0)

    def test_add_film(self):
        actor = Actor('Nicolas Zanforlini')
        actor.add_film('Lord of war')
        self.assertEqual(len(actor.films), 1)
        self.assertEqual(actor.films[0], 'Lord of war')
        actor.add_film('Wow')
        self.assertEqual(len(actor.films), 2)
        self.assertEqual(actor.films[0], 'Lord of war')
        self.assertEqual(actor.films[1], 'Wow')

    def test_load(self):
        actor = Actor('Nicolas Zanforlini')
        actor.add_film('Lord of war')
        actor.add_film('Wow')
        actor.load(db)
        actor_document = db.actors.find_one({'name' : 'Nicolas Zanforlini'})
        self.assertIsNotNone(actor_document)
        self.assertEqual(actor_document.get('name'), 'Nicolas Zanforlini')
        self.assertEqual(actor_document.get('films'), ['Lord of war', 'Wow'])

        db.actors.delete_many({'name' : 'Nicolas Zanforlini'})

if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    db = client.unittest_pymongo

    unittest.main()

    client.close()
