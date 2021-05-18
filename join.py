import discord
from discord.ext import commands

bot = commands.Bot(command_prefix ="__")
@bot.event
async def on_ready():
    print("MineBOT est prêt à l'usage !")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with a lot of users"))

@bot.command(pass_context = True)
async def join(ctx):
    voice_state = ctx.author.voice
    if voice_state is None:
        await ctx.send("Oops... Looks like you're not in a channel.")
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send("MineBOT is in your channel.")

bot.run("token")