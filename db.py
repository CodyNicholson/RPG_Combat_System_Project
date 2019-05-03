import pymongo
import random
from ship import Ship

# The default port used by MongoDB is 27017
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Declare the database
db = client.rpg_combat_system

# Declare the collection
collection = db.ships

def create_ship(*, name:str, typ:str):
    # A dictionary that represents the document to be inserted
    post = {
        'name': name,
        'lvl': 1,
        'exp': 0,
        'typ': typ,
        'hp': random.randint(500,1000),
        'atk': random.randint(100,300),
        'res': random.randint(50,200),
        'spd': random.randint(80, 150)
    }
    print("\nNew Ship:")
    print(post + "\n")
    # Insert the document into the database
    # The database and collection, if they don't already exist, will be created at this point
    collection.insert_one(post)

def create_ship_hardcode(*, name:str, lvl:int, exp:int, typ:str, hp:int, atk:int, res:int, spd:int):
    # A dictionary that represents the document to be inserted
    post = {
        'name': name,
        'lvl': lvl,
        'exp': exp,
        'typ': typ,
        'hp': hp,
        'atk': atk,
        'res': res,
        'spd': spd
    }
    # Insert the document into the database
    # The database and collection, if they don't already exist, will be created at this point
    collection.insert_one(post)

def get_ships() -> list:
    ships_cursor = db.ships.find()
    ship_list = []
    for ship in ships_cursor:
        ship_list.append(Ship(name=ship['name'], lvl=ship['lvl'], exp=ship['exp'], typ=ship['typ'], hp=ship['hp'], atk=ship['atk'], res=ship['res'], spd=ship['spd']))
    return ship_list

def create_ship_list() -> list:
    ship_list = get_ships()
    if len(ship_list) < 1:
        create_ship(name="Delphinus", typ="Cruiser")
        create_ship(name="Iron Clad", typ="Bomber")
        create_ship(name="Lynx", typ="Glider")
        ship_list = get_ships()
    return ship_list
