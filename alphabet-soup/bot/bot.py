import discord

from bot.bot_config import BotConfig
from bot.embed_builder import EmbedBuilder
from discord.ext import commands
from discord.ext.commands.core import command

class AlphabetSoupBot:
    def __init__(self, config_file: str, *, command_prefix: str='&'):
        self.config = BotConfig(config_file)
        self.intents = discord.Intents.default()
        self.bot = commands.Bot(command_prefix=command_prefix, intents=self.intents)
        self.bot.remove_command('help') # Will replace this with our custom help command

    def run(self):
        cogs = ['bot.cogs.game_cog']
        for cog in cogs:
            self.bot.load_extension(cog)
        
        @self.bot.event
        async def on_ready():
            print('Logged in as {0} - {1}'.format(self.bot.user.name, self.bot.user.id))
            print('------------')
            await self.bot.change_presence(activity=discord.Game(name='Alphabet Soup | &help'))
        
        self.bot.run(self.config.BOT_TOKEN)