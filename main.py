import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import has_role
import os
import random
import info
import requests
from flask import Flask
from threading import Thread
import psutil
import keepalive

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


def colour():
    colours = [
        0, 0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694,
        0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xe67e22,
        0xa84300, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a, 0x7289da, 0x99aab5
    ]
    return random.choice(colours)


@client.event
async def on_ready():
    await tree.sync()
    print(f'logged in as {client.user}')
    keepalive.keep_alive()


# @tree.command(description = 'Replies with Pong!')
# async def ping(interaction: discord.Interaction):
#   await interaction.response.send_message(content = f'Pong!   `{round(client.latency*100)}ms`')

# @tree.command(description = 'shows sources')
# async def credits(interaction:discord.Interaction):
#   embed = discord.Embed(title = 'Credits', description = 'Samaritans of Singapore - https://www.sos.org.sg/\nImgur - https://imgur.com/', color = colour())
#   embed.set_footer(text = 'Here are our sources🙂')
#   await interaction.response.send_message(embed = embed)


@tree.command(
    description='Shows more information about the creators behind HopeHub')
async def about_us(interaction: discord.Interaction):
    embed = discord.Embed(
        title='About us',
        description=
        'This bot is an initiative by Catholic High School’s I.O.N society to tackle depression.',
        color=colour())
    # embed.set_footer(text = 'https://github.com/TheInfamousPro/Hope-Bot\nthis is the github repo')
    await interaction.response.send_message(embed=embed)


# @tree.command(description = 'adds item to blacklist')
# async def blacklist_add(interaction:discord.Interaction, text:str):
#   info.blacklist.append(text)
#   await interaction.response.send_message(content = f'{text} has been added to the blacklist')

# @tree.command(description = 'removes item from blacklist')
# async def blacklist_remove(interaction:discord.Interaction, text:str):
#   text = text.lower()
#   try:
#     info.blacklist.remove(text)
#     await interaction.response.send_message(content = f'{text} has been removed from the blacklist successfully')
#   except ValueError:
#     await interaction.response.send_message(content = f'{text} is not in the blacklist')
#   except:
#     await interaction.response.send_message(content = f'An error has occured')
# @tree.command(description = 'sends the blacklsit')
# async def blacklist_view(interaction:discord.Interaction):
#   await interaction.response.send_message(content = '\n'.join(info.blacklist))


@tree.command(description='Show server statistics')
async def stats(interaction: discord.Interaction):
    embed = discord.Embed(
        title='System Resource Usage',
        description='See the CPU and memory usage of our HopeHub server')
    embed.add_field(name='📟CPU usage',
                    value=f'{round(psutil.cpu_percent())}%',
                    inline=False)
    embed.add_field(name='💾Memory usage',
                    value=f'{round(psutil.virtual_memory().percent)}%',
                    inline=False)
    embed.add_field(
        name='💾Available memory',
        value=
        f'{round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)}%',
        inline=False)
    await interaction.response.send_message(embed=embed)


@client.event
async def on_message(ctx):
    if ctx.author.bot:
        return
    for i in info.blacklist:
        if i in str(ctx.content).lower():
            await ctx.reply(
                f'{random.choice(info.Greeting)} {ctx.author.mention} 👋\n**{random.choice(info.Sign)}**. {random.choice(info.Comfort)}.'
            )
            embed = discord.Embed(
                title='Help is available.',
                description='Call 1-767 to speak to someone today.')
            embed.set_footer(text="We’re in this together 💪")
            embed.set_image(url='https://i.imgur.com/Zs8E4sp.png')
            await ctx.channel.send(embed=embed)

client.run('MTAxMjY2Mjc2Mjc4ODM3NjY1Ng.'+'GzJvcV.1k-JXzTvUT2EeaLEpUwSRafbp-r2XcMqUhcXzw')
