import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

bot = commands.Bot(command_prefix ="")
@bot.event
async def on_ready():
    print("MineBOT est prêt à l'usage !")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with a lot of users"))
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Looks like you are not allowed to do this...")
        
@bot.command(name ="clear", pass_context = True)
@has_permissions(manage_messages=True)
async def clearmessage(ctx, nbr = 5):
    await ctx.channel.purge(limit=nbr+1)

bot.run("token")