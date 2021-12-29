class Player:
    def __init__(self, user_id: int, found_words: list=[]):
        self.user_id = int(user_id)
        self.found_words = found_words
    
    @staticmethod
    def create_from_id(user_id: int):
        return Player(user_id)
    
    def __str__(self):
        return "<@{0}>".format(self.user_id)

    def find_word(self, word: str):
        if word in self.found_words:
            raise ValueError("Already found word " + word)

        self.found_words.append(word.upper())

class PlayerMapper:
    @staticmethod
    def map_to_db_dict(player: Player, *, exclude_words: bool=False):
        db_dict = { 'user_id': str(player.user_id) }
        if not exclude_words:
            db_dict['found_words'] = player.found_words
        return db_dict