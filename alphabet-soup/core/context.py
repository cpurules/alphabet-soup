class Context:
    def __init__(self, guild_id: int, channel_id: int):
        self.guild_id = int(guild_id)
        self.channel_id = int(channel_id)
    
    @staticmethod
    def create_from_ctx(ctx):
        if ctx.guild is None:
            raise ValueError('Supplied context does not have a guild')

        return Context(ctx.guild.id, ctx.channel.id)
    
    def as_db_dict(self):
        return {
            'guild_id': str(self.guild_id),
            'channel_id': str(self.channel_id)
        }