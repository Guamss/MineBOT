import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import cog_admin
import cog_basic
from opgg_scraper.monscraper import Opggtrack

bot = commands.Bot(command_prefix ="__", allowed_mentions =  discord.AllowedMentions(everyone = True, users = True))
@bot.event
async def on_ready():
    print("MineBOT state : Ready")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="__commandlist for command list"))
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Looks like you are not allowed to do this...")

    

bot.add_cog(cog_basic.CogBasic(bot))
bot.add_cog(cog_admin.CogAdmin(bot))
bot.run("token")