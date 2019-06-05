import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time
import random
from random import *
import os

import dict
from dict import *


client = discord.Client()
status = ['COONS', 'COOOOOOONS']


async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    
    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(activity=discord.Activity(name=current_status))
        await asyncio.sleep(2)
               
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(name='Online!'))
    print("Bot is ready")

@client.event
async def on_message(message):
    mess = message.content.lower()
    auth = message.author
    channel = message.channel
    rnd = randint(1,10)
    if auth == client.user: return
    else:
        if rnd == 1:
            rnd = randint(0,len(coonsdict) - 1)
            await message.add_reaction(coonsdict[coons[rnd]])
        
            
client.loop.create_task(change_status())
client.run(os.environ['BOT_TOKEN'])
