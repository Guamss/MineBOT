import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

bot = commands.Bot(command_prefix ="__")
@bot.event
async def on_ready():
    print("MineBOT est prêt à l'usage !")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with a lot of users"))

@bot.command(name ="clear", pass_context = True)
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def clearmessage(ctx, nbr = 5):
    await ctx.channel.purge(limit=nbr+1)
@clearmessage.error
async def clearmessage_error(error, ctx):
    if isinstance(error, CheckFailure):
        await bot.send_message(ctx.message.channel, "Looks like you're not authorized to do this...")

bot.run("token")