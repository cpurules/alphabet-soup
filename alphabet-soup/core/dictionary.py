import os.path

from core.dice import Dice
from enum import Enum

class Dictionary(Enum):
    @staticmethod
    def _load_lines_from_file(path: str):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
        with open(path, 'r') as f:
             return [line.strip().upper() for line in f.readlines()]
    
    SOWPODS_ENGLISH = {
        'words': _load_lines_from_file.__func__('resources/dicts/sowpods.txt'),
        'valid_dice': [Dice.CLASSIC_ENGLISH, Dice.NEW_ENGLISH, Dice.BIG_ENGLISH]
    }