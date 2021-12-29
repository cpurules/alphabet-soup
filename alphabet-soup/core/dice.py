import os.path
import random

from enum import Enum
from math import sqrt

class Dice(Enum):
    @staticmethod
    def _load_from_file(path: str):
        dice = []
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), path)
        with open(path, 'r') as f:
            file_lines = f.readlines()
            for line in file_lines:
                faces = line.upper().strip().split(" ")
                # Validate faces
                # 1-3 letters are allowed
                face_lengths = [len(face) for face in faces]
                if min(face_lengths) == 0:
                    raise ValueError("Cannot have empty faces")
                elif max(face_lengths) > 3:
                    raise ValueError("Cannot have faces with more than 3 letters")
                    
                dice.append(faces)
        
        # I have accepted that this is imperfect for large values
        # However, we'll handwave this away by capping at an 8x8 board
        # Even the largest version of the original game only goes to 6x6 :)
        dice_count = len(dice)
        if dice_count == 0:
            raise ValueError("Cannot load empty list of dice")
        elif dice_count > 64:
            raise ValueError("Cannot load more than 64 dice (8x8 board) (tried to load {0})".format(dice_count))
        
        cube_width = sqrt(dice_count)
        if int(cube_width) != cube_width:
            raise ValueError("Cannot load a non-perfect square number of dice (tried to load {0})".format(dice_count))

        return dice
    
    CLASSIC_ENGLISH = _load_from_file.__func__('resources/dice/classic_english.txt')
    NEW_ENGLISH = _load_from_file.__func__('resources/dice/new_english.txt')
    BIG_ENGLISH = _load_from_file.__func__('resources/dice/big_english.txt')
    
    def roll_all(self):
        dice_list = self.value
        shuffled_dice = random.sample(dice_list, len(dice_list))

        letters = []
        for die_faces in shuffled_dice:
            letters.extend(random.sample(die_faces, 1))

        return letters