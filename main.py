import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time
import random
import os

import coonsdict
from coonsdict import *

client = commands.Bot(command_prefix = "-")
client.remove_command('help')
status = ['COONS', 'COOOOOOONS']

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    
    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(2)
           
        
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Online!'))
    print("Bot is ready")

@client.event
async def on_message(message):
    mess = message.content.lower()
    auth = message.author
    if not auth.id == "585341561345409044":
        if "hi" in mess:
            await client.send_message(message.channel, "hi")

@client.command(pass_context=True)
async def help(ctx):

    embed = discord.Embed(
        color = discord.Color.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='**-ping**', value='Returns Pong!', inline=False)
    
    embed.add_field(name='**-say <string>**', value='Tells the bot to say something.', inline=False)
    

    await client.say(embed=embed) #send_message(author, embed=embed)

async def ping():
    await client.say('Pong!')
    
async def say(*args):
    output = ' '
    for word in args:
        output += word
        output += ' '
    await client.say(output)
    
    
    
client.loop.create_task(change_status())
client.run("NTg1MzQxNTYxMzQ1NDA5MDQ0.XPYQsA.AwRxKpIBUn5J_A0f89nU0DfVbNs")    



#tbd
