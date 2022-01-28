import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">>古代靈異雙頭戰象已被召喚<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(936520716390653992)
    await channel.send(f'{member} 滑進垃圾車')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(936520716390653992)
    await channel.send(f'{member} 高歌離席')

bot.run('OTM2MjcyMTk1NDkwMDU0MTk0.YfKxbg.mCZj7Bg-8VhhSpt7Y-K9630gyoA')