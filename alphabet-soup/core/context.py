class Context:
    def __init__(self, guild_id: int, channel_id: int, owner_id: int):
        self.guild_id = int(guild_id)
        self.channel_id = int(channel_id)
        self.owner_id = int(channel_id)
    
    @staticmethod
    def create_from_ctx(ctx):
        if ctx.guild is None:
            raise ValueError('Supplied context does not have a guild')

        return Context(ctx.guild.id, ctx.channel.id, ctx.author.id)

class ContextMapper:
    @staticmethod
    def map_to_db_dict(context: Context):
        return {
            'guild_id': str(context.guild_id),
            'channel_id': str(context.channel_id),
            'owner_id': str(context.owner_id)
        }