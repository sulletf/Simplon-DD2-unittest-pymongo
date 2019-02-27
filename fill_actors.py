from pymongo import MongoClient
from MongoDB import *
import re

client = MongoClient('localhost', 27017)
db = client.unittest_pymongo
films = db.films

actors = {}

for film in films.find():

  for dirty_actor_name in film.get("actors"):
    clean_actor_name = dirty_actor_name.replace("\n","").strip()

    actor_object = actors.get(clean_actor_name)

    if actor_object is None:
      actor_object = Actor(clean_actor_name)
      actors[clean_actor_name] = actor_object

    actor_object.add_film(film.get("title"))


for actor_object in actors.values():
  actor_object.load(db)


