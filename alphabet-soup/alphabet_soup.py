import os

from bot.bot import AlphabetSoupBot
from core.board import Board
from core.dice import Dice

config_file = os.getenv('CONFIG_FILE')

bot = AlphabetSoupBot(config_file)
bot.run()