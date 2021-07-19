import discord
from discord.ext import commands
import random
from opgg_scraper.monscraper import Opggtrack

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
        
    @commands.command()
    async def punch(self, ctx):
        gifs = ["gif/punch/punch0.gif", "gif/punch/punch1.gif", "gif/punch/punch2.gif"]
        random.shuffle(gifs)
        await ctx.send("Vous tabassez (à mort) un gros fils de pute", file=discord.File(gifs[0]))
        
    @commands.command()
    async def commandlist(self, ctx):
        await ctx.send(file = discord.File("help/help.txt"))

    @commands.command()
    async def opgg(self, ctx, username, region):
        tracker = Opggtrack(username, region)
        await ctx.send(f"{username} en {region}")
        await ctx.send(f"rank : {tracker.get_ranksolo()} | Classé Solo/Duo")
        await ctx.send(f"rank : {tracker.get_rankflex()} | Flex 5:5")
        await ctx.send(f"winrate : {tracker.get_winratio()}")
        await ctx.send(f"kda ratio : {tracker.get_kdaratio()}")
        

        