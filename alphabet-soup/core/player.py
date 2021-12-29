class Player:
    def __init__(self, user_id: int, found_words: list=[]):
        self.user_id = int(user_id)
        self.found_words = found_words
    
    @staticmethod
    def create_from_id(user_id: int):
        return Player(user_id)
    
    def find_word(self, word: str):
        if word in self.found_words:
            raise ValueError("Already found word " + word)

        self.found_words.append(word.upper())