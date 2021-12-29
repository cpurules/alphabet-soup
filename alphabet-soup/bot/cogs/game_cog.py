import asyncio
import discord

from discord.ext import commands
from bot.embed_builder import EmbedBuilder

class GameCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='start')
    async def start_game(self, ctx):
        await ctx.send(content='You started a game!')
        #response_embed = EmbedBuilder().set_title("Alphabet Soup - New Game")
        #game_fields = {
        #    '_key': ctx.message.id,
        #    'owner': ctx.author.id,
        #    'guild': GameGuild.create_from_ctx(ctx)
        #}
        #try:
        #    new_game = Game.create_new(**game_fields)
        #    await ctx.send(content='Created new game!')
        #except Exception as e:
        #    await ctx.send(content=str(e))

def setup(bot):
    bot.add_cog(GameCog(bot))