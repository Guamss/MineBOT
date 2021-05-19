import discord
from discord.ext import commands

class CogBasic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def join(self, ctx):
        voice_state = ctx.author.voice
        if voice_state is None:
            await ctx.send("Oops... Looks like you're not in a channel.")
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("MineBOT is in your channel.")

    @commands.command()
    async def leave(self, ctx):
        voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
        if voice is None:
            await ctx.send("I need to be in a voice channel to do this.")
        await ctx.message.guild.voice_client.disconnect()
        await ctx.send("Poof ! Thanks for using me !")