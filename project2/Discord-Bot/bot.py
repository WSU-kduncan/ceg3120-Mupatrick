import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
#TOKEN='ODg4MjY0NjE1NTQ3NTIzMTky.YUQK4w.jbJsurWN95Q284aNPis2LLIlUM4'
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    question = [
        'If we shouldn’t eat at night, why is there a light in the fridge?',
        'If Cinderella’s shoe fit perfectly, then why did it fall off?',
        
    ]

    fun_joke = [
        'Your life can\'t fall apart if you never had it together.',
        'Some people just need a high-five. In the face. With a chair.',
        ]

    if message.content == 'question!':
        display1 = random.choice(question)
        await message.channel.send(display1)

    elif message.content == 'fun!':
        display2 = random.choice(fun_joke)
        await message.channel.send(display2)

client.run(TOKEN)
