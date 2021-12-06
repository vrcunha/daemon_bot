import os
from discord import Client
from utils.dice_utils import roll
from dotenv import load_dotenv

load_dotenv()

client = Client()

@client.event
async def on_ready():
    print(f'The {client.user} bot is online.')

@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return

    if msg.startswith('/Hello'):
        await message.channel.send(f'Hello @{message.author}')

    if msg.startswith('/r'):
        roll_dice = msg.split('/r ')[1]
        await message.channel.send(roll(roll_dice))

client.run(os.getenv('TOKEN')) 
