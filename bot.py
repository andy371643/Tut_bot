import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">>古代靈異雙頭戰象已被召喚<<")

bot.run('OTM2MjcyMTk1NDkwMDU0MTk0.YfKxbg.452xfOZNGrPgatu5bhLQ505H5YY')