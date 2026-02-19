from enum import Enum


class user_position(str, Enum):
    height = '/user_data/height'
    weight = '/user_data/weight'
    physique = '/user_data/physique'
    program = '/user_prog'


class tren_group (str, Enum):
    nogi_ladizhka = 'Лодыжка'
    nogi_bedro = 'opopo'