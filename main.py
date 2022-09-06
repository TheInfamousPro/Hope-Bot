import discord
from discord.utils import get
import os
import requests
import config
import random
client = discord.Client(intents=discord.Intents.default())
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(ctx):
  if ctx.author.bot:
    return
  for i in config.blacklist:
    if i in str(ctx.content).lower():
      await ctx.reply(f'{random.choice(config.Greeting)} {ctx.author.mention} 👋\n**{random.choice(config.Sign)}**. {random.choice(config.Comfort)}.')
      embed = discord.Embed(title = 'Help is available.', description = 'Call 1-767 to speak to someone today.')
      embed.set_footer(text = "We’re in this together 💪")
      embed.set_image(url = 'https://i.imgur.com/Zs8E4sp.png')
      await ctx.channel.send(embed = embed)
client.run(open('C:\\Users\\ZHANG LINJIE\Desktop\\Hope Bot\\token.txt.txt','r').read())
