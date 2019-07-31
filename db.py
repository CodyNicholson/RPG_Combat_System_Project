import pymongo
import random
from ship import Ship

# The default port used by MongoDB is 27017
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Declare the database
db = client.rpgdb

# Declare the collection
collection = db.ships

def create_ship(*, name:str, typ:str):
    # TODO check if name already exists
    rand_vals = {'hp': [700, 900], 'atk': [300, 500], 'res': [100, 200], 'spd': [150, 250]}
    if typ == "Bomber":
        rand_vals = {'hp': [800, 1000], 'atk': [350, 550], 'res': [150, 250], 'spd': [50, 150]}
    elif typ == "Glider":
        rand_vals = {'hp': [600, 800], 'atk': [250, 450], 'res': [50, 150], 'spd': [250, 350]}
    post = {
        'name': name,
        'lvl': 1,
        'exp': 0,
        'typ': typ,
        'hp': random.randint(rand_vals['hp'][0],rand_vals['hp'][1]),
        'atk': random.randint(rand_vals['atk'][0],rand_vals['atk'][1]),
        'res': random.randint(rand_vals['res'][0],rand_vals['res'][1]),
        'spd': random.randint(rand_vals['spd'][0],rand_vals['spd'][1])
    }
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

def delete_ship(*, name:str):
    all_ships = get_ships()
    for ship in all_ships:
        ship_name = ship.get_name()
        if ship_name == name:
            collection.delete_one({"name" : ship_name})
            return
    print("There is no ship in the harbor with that name")

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

def save_ship(*, ship:Ship) -> None:
    ship_name = ship.get_name()
    updated_ship = {
        'name': ship_name,
        'lvl': ship.get_lvl(),
        'exp': ship.get_exp(),
        'typ': ship.get_typ(),
        'hp': ship.get_base_hp(),
        'atk': ship.get_base_atk(),
        'res': ship.get_base_res(),
        'spd': ship.get_base_spd()
    }
    collection.update({"name": ship_name}, {"$set": updated_ship}, upsert = True)
