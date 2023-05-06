from unit import BaseUnit
from base import Arena
from classes import unit_classes
from equipment import Equipment

arena = Arena()

heroes = {
    "player": BaseUnit,
    "enemy": BaseUnit
}

equipment = Equipment()
weapons = equipment.get_weapons_names()
armors = equipment.get_armors_names()

forms_create_units = {
    "classes": unit_classes,
    "weapons": weapons,
    "armors": armors
}
