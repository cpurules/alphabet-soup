from core.dice import Dice
from core.dictionary import Dictionary
from core.context import Context, ContextMapper
from core.player import Player, PlayerMapper

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
    
    def start(self):
        active_game = ActiveGame(self._key, self.context, self.players, self.dictionary,
                            self.dice, self.time_limit, datetime.now())
        # update game in database TODO
        return active_game

class ActiveGame(Game):
    def __init__(self,
                    _key: int, context: Context, players: list[Player],
                    dictionary: Dictionary, dice: Dice, time_limit: timedelta,
                    started_at: datetime):
        super().__init__(_key, context, players, dictionary, dice, time_limit)
        self.started_at = started_at
    
    def start(self):
        raise RuntimeError("Cannot start an active game")

class EndedGame(Game):
    def __init__(self,
                    _key: int, context: Context, players: list[Player],
                    dictionary: Dictionary, dice: Dice, time_limit: timedelta,
                    started_at: datetime, winner: Player, longest_words: list):
        super().__init__(_key, context, players, dictionary, dice, time_limit)
        self.started_at = started_at
        self.winner = winner
        self.longest_words = longest_words
    
    def start(self):
        raise RuntimeError("Cannot start an ended game")

class GameMapper:
    @staticmethod
    def map_to_db_dict(game: Game):
        db_dict = {
            '_key': str(game._key),
            'context': ContextMapper.map_to_db_dict(game.context),
            'players': [PlayerMapper.map_to_db_dict(player) for player in game.players],
            'dictionary': game.dictionary.name,
            'dice': game.dice.name,
            'time_limit': game.time_limit
        }
        if isinstance(game, ActiveGame):
            db_dict.update({
                'started_at': game.started_at
            })
        if isinstance(game, EndedGame):
            db_dict.update({
                'started_at': game.started_at,
                'winner': PlayerMapper.map_to_db_dict(game.winner, exclude_words=True),
                'longest_words': game.longest_words
            })
        return db_dict