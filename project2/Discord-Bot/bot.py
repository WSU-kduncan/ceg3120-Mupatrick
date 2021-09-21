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

    my_favority_quotes = [
        'If you cannot do great things, do small things in a great way ',
        'Do what you can, with what you have, where you are',
        'Do not let what you cannot do interfere with what you can do',
        'Everything has beauty, but not everyone can see.',

        (
            'Never regret anything that made you smile,😀😀 '
            'whatever you do do it well!.😀'
        ),
    ]

    just_laugh_quotes = [
        'My mother always used to say: The older you get, the better you get, unless you’re a banana.',
        'Before you marry a person, you should first make them use a computer with slow internet to see who they real are.',
        'When your mother asks, ‘Do you want a piece of advice?’ it is a mere formality. It doesn’t matter if you answer yes or no. You’re going to get it anyway.',
        'Never follow anyone else’s path. Unless you’re in the woods and you’re lost and you see a path. Then by all means follow that path',
    ]

    if message.content == 'laugh!':
        response = random.choice(just_laugh_quotes)
        await message.channel.send(response)
    elif message.content == 'favority!':
        response2 = random.choice(my_favority_quotes)
        await message.channel.send(response2)

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
