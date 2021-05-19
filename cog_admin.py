import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class CogAdmin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, nbr = 5):
        await ctx.channel.purge(limit=nbr+1)