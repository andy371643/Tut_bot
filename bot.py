import discord
from discord.ext import commands
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

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

@bot.command()
async def ping(ctx):
    await ctx.send(f'延遲時間{round(bot.latency*1000)} 秒')

bot.run(jdata['TOKEN'])