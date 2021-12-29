import asyncio
import core.context
import core.dice
import core.dictionary
import core.game
import core.player
import discord

from bot.embed_builder import EmbedBuilder
from datetime import timedelta
from discord.ext import commands

class GameCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='play')
    async def start_game(self, ctx):
        response_embed = EmbedBuilder().set_title("Alphabet Soup - New Game")
        
        game_fields = {
            '_key': ctx.message.id,
            'context': core.context.Context.create_from_ctx(ctx),
            'players': [core.player.Player.create_from_id(ctx.author.id)],
            'dictionary': core.dictionary.Dictionary.SOWPODS_ENGLISH,
            'dice': core.dice.Dice.NEW_ENGLISH,
            'time_limit': timedelta(minutes=3)
        }
        try:
            new_game = core.game.Game(**game_fields)
            response_embed = response_embed.set_description("You've created a new lobby for Alphabet Soup!") \
                                            .append_to_description("Below are the current game options:") \
                                            .append_to_description("") \
                                            .append_to_description("Players: {0}".format(" ".join([str(player) for player in new_game.players]))) \
                                            .append_to_description("Dictionary: `{0}`".format(new_game.dictionary.name)) \
                                            .append_to_description("Dice Set: `{0}`".format(new_game.dice.name)) \
                                            .append_to_description("Time Limit: `{0}`".format(new_game.time_limit)) \
                                            .append_to_description("") \
                                            .append_to_description("Use `&join` to join the game!") \
                                            .append_to_description("Hosts: use `&options` to update game options, or `&start` to begin the game")
            await ctx.send(embed=response_embed.build())
        except Exception as e:
            await ctx.send(content=str(e))

def setup(bot):
    bot.add_cog(GameCog(bot))