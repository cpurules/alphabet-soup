import asyncio
import core.context
import core.dice
import core.dictionary
import core.game
import core.player
import discord

from bot.embed_builder import EmbedBuilder
from discord.ext import commands

class GameCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='start')
    async def start_game(self, ctx):
        await ctx.send(content='You started a game!')
        response_embed = EmbedBuilder().set_title("Alphabet Soup - New Game")
        
        game_fields = {
            '_key': ctx.message.id,
            'context': core.context.Context.create_from_ctx(ctx),
            'players': [core.player.Player.create_from_id(ctx.author.id)],
            'dictionary': core.dictionary.Dictionary.SOWPODS_ENGLISH,
            'dice': core.dice.Dice.NEW_ENGLISH,
            'time_limit': 180
        }
        try:
            new_game = core.game.Game(**game_fields)
        except Exception as e:
            await ctx.send(content=str(e))

def setup(bot):
    bot.add_cog(GameCog(bot))