from core.dice import Dice
from core.dictionary import Dictionary
from core.context import Context
from core.player import Player

from datetime import datetime, timedelta

class Game:
    def __init__(self,
                    _key: int, context: Context, players: list[Player],
                    dictionary: Dictionary, dice: Dice, time_limit: timedelta):
        self._key = int(_key)
        self.context = context
        self.players = players
        self.dictionary = dictionary
        self.dice = dice
        self.time_limit = time_limit

class ActiveGame(Game):
    def __init__(self,
                    _key: int, context: Context, players: list[Player],
                    dictionary: Dictionary, dice: Dice, time_limit: timedelta,
                    started_at: datetime):
        super().__init__(_key, context, players, dictionary, dice, time_limit)
        self.started_at = started_at

class EndedGame(Game):
    def __init__(self,
                    _key: int, context: Context, players: list[Player],
                    dictionary: Dictionary, dice: Dice, time_limit: timedelta,
                    started_at: datetime, winner: Player, longest_words: list):
        super().__init__(_key, context, players, dictionary, dice, time_limit)
        self.started_at = started_at
        self.winner = winner
        self.longest_words = longest_words