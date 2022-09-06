import discord
from discord.utils import get
import os
import requests
import info
import random
import logger
client = discord.Client()
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(ctx):
  if ctx.author == client.user:
    return
  if ctx.content.startswith('$blacklist add'):
    info.blacklist.append(str(ctx.content).split(' ')[3])
    await ctx.reply(str(ctx.content).split()[3] + 'has been added to blacklist')
    await ctx.channel.send('If you do not see a message, an error has occured')
  elif ctx.content.startswith('$purge'):
    await ctx.channel.purge(limit = int(str(ctx.content).split(' ')[1]) + 1)
  for i in info.blacklist:
    if i in str(ctx.content).lower():
      await ctx.reply(f'{random.choice(info.Greeting)} {ctx.author.mention} 👋\n**{random.choice(info.Sign)}**. {random.choice(info.Comfort)}.')
      embed = discord.Embed(title = 'Help is available.', description = 'Call 1-767 to speak to someone today.')
      embed.set_footer(text = "We’re in this together 💪")
      embed.set_image(url = 'https://i.imgur.com/Zs8E4sp.png')
      await ctx.channel.send(embed = embed)
try:
  client.run(os.environ['Token'])
except discord.errors.HTTPException:
  print('restarting ......')
  os.system('python restarter.py')
os.system('python keepalive.py')
