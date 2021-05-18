import discord
from discord.ext import commands

bot = commands.Bot(command_prefix ="__")

@bot.event
async def on_ready():
    print("MineBOT est prêt à l'usage !")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with a lot of users"))

@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice is None:
        await ctx.send("I need to be in a voice channel to do this.")
    await ctx.message.guild.voice_client.disconnect()
    await ctx.send("Poof ! Thanks for using me !")

bot.run("token")