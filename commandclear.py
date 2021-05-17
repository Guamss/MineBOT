import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure

bot = commands.Bot(command_prefix ="prefix", allowed_mentions =  discord.AllowedMentions(everyone = True, users = True))
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="I'm a default bot!"))
    print("")

@bot.command(name ="clear", pass_context = True)
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def clearmessage(ctx, nbr = 5):
    await ctx.channel.purge(limit=nbr+1)
@clearmessage.error
async def clearmessage_error(error, ctx):
    if isinstance(error, CheckFailure):
        await bot.send_message(ctx.message.channel, "On dirait que tu n'est pas autorisé à faire ceci...")





bot.run("token")