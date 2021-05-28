import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import cog_admin
import cog_basic

bot = commands.Bot(command_prefix ="__", allowed_mentions =  discord.AllowedMentions(everyone = True, users = True))
@bot.event
async def on_ready():
    print("MineBOT est prêt à l'usage !")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with a lot of users"))
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Looks like you are not allowed to do this...")

bot.add_cog(cog_basic.CogBasic(bot))
bot.add_cog(cog_admin.CogAdmin(bot))
bot.run("ODQyMTQ4MjE4OTEyNTA1ODk2.YJxFpQ.eOEA_t22xICJdkQMt4O5F4Vn2qw")