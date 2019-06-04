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

client = commands.Bot(command_prefix = "-")
client.remove_command('help')

                
@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    mess = message.content.lower()
    auth = message.author
    rnd = randint(0,100)
    if not auth.id == "585341561345409044":
        if rnd in range(10):
            rnd = randint(0,len(coonsdict) - 1)
            if message.content.find('EMOJI_NAME'):
                for x in client.get_all_emojis():
                    if x.id == coonsdict[coons[rnd]]:
                        await client.add_reaction(message, x)
        if "hi" in mess:
            await client.send_message(message.channel, "hi")

async def get_reaction(message,i):
    index = randint(0,len(reactionsdict[inmsg[i]]) - 1)
    try:
       await client.add_reaction(message,reactionsdict[inmsg[i]][index])
    except:
        if message.content.find('EMOJI_NAME'):
            for x in client.get_all_emojis():
                if x.id == reactionsdict[inmsg[i]][index]:
                    await client.add_reaction(message, x)

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
client.run(os.environ['BOT_TOKEN'])    



#tbd
