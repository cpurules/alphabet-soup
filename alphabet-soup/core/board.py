import random

from core.dice import Dice
from math import sqrt

class Board:
    @staticmethod
    def create_from_dice(dice: Dice):
        dice_list = dice.value
        shuffled_dice = random.sample(dice_list, len(dice_list))

        letters = []
        for die_faces in shuffled_dice:
            letters.extend(random.sample(die_faces, 1))

        return Board(letters)

    # letters is interpreted as left-to-right, top-to-bottom
    def __init__(self, letters: list):
        if len(letters) == 0:
            raise ValueError("Cannot create board with empty list of letters")

        cube_width = sqrt(len(letters))
        if int(cube_width) != cube_width:
            raise ValueError("Cannot create board with non-square number of letters")
        
        self.letters = letters
    
    @property
    def cube_width(self):
        return int(sqrt(len(self.letters)))

    def __str__(self):
        cube_text_width = 4 * self.cube_width + 1 # 2+, 3n letter, (n-1) separator
        top_bottom_border = "+" + ("-" * (cube_text_width - 2)) + "+"
        middle_separator = "|" + ("+".join(["---"] * self.cube_width)) + "|" # surrounding pipes, ---+ per letter except for the last letter has no +

        board_lines = [top_bottom_border]
        for row in range(0, self.cube_width):
            letters_text = []

            for column in range(0, self.cube_width):
                row_letter = self.letters[self.cube_width * row + column]
                if len(row_letter) == 1:
                    row_letter = " {0} ".format(row_letter)
                elif len(row_letter) == 2:
                    row_letter = " {0}".format(row_letter)
                
                letters_text.append(row_letter)

            board_lines.append("|{0}|".format("|".join(letters_text)))
            
            if not row == (self.cube_width - 1):
                board_lines.append(middle_separator)

        board_lines.append(top_bottom_border)

        return "\n".join(board_lines)
    
    def _idx_to_row_col(self, idx: int):
        if idx < 0 or idx >= len(self.letters):
            raise IndexError("Supplied index is out of range for this board")
        
        row = int(idx / self.cube_width)
        col = idx - (self.cube_width * row)
        return (row, col)
    
    def _row_col_to_idx(self, row_col: tuple):
        row, col = row_col
        if row < 0 or row >= self.cube_width:
            raise IndexError('Supplied row is out of range for this board')
        if col < 0 or col >= self.cube_width:
            raise IndexError('Supplied column is out of range for this board')
        
        return (self.cube_width * row + col)
    
    def contains_string(self, string: str, *, visited: list=[], start_idx: int=None):
        if len(string) == 0:
            return True

        start_char = str(string[0])
        rest = str(string[1:])

        # Get all locations our search character appears on the board
        all_start_indexes = [idx for idx, letter in enumerate(self.letters) if letter == start_char]
        
        # If we don't have a start_idx, then any of the first character appearances are valid
        if start_idx is None:
            valid_start_indexes = all_start_indexes
        # If we have a start_idx, we need to look at +- 1 row/col from start_idx and try to match
        else:
            valid_start_indexes = []
            start_location = self._idx_to_row_col(start_idx)
            for col_adjust in [-1, 0, 1]:
                for row_adjust in [-1, 0, 1]:
                    if col_adjust == 0 and row_adjust == 0:
                        # Can't re-use the tile we're already on
                        continue
                    new_location = (start_location[0] + row_adjust, start_location[1] + col_adjust)
                    # If the index is out of bounds (i.e. we're at a border), we'll skip
                    try:
                        test_index = self._row_col_to_idx(new_location)
                        # Make sure we haven't already used this test_index and that it actually has our letter
                        if not test_index in visited and test_index in all_start_indexes:
                            valid_start_indexes.append(test_index)
                    except IndexError:
                        continue
        
        # If we don't have any valid start indexes, then we can't use this letter and ergo can't find the string
        if len(valid_start_indexes) == 0:
            return False

        # Now, valid_start_indexes contains all letter indexes where we can start the string we're searching for
        # So, for all valid_start_indexes, check contains_string for the rest of our string, marking the valid_start_index as visited and settings it as the start_idx
        return any(
            [self.contains_string(rest,
                                    visited=(visited + [start_index]),
                                    start_idx=start_index)
                for start_index in valid_start_indexes]
        )