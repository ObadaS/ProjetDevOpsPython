import os
import random
import discord

from dotenv import load_dotenv

# Pour charger le fichier .env, où les variables sensitives sont stocké
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Necessaire pour les droits du Bot, sinon certaines fonctionnalités ne seront pas disponible : https://discordpy.readthedocs.io/en/latest/intents.html
intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    # Etape 1
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )


# Etape 2
@client.event
async def on_member_join(member):
    # Pour envoyer le message dans le channel general (de id 997471760029073542)
    channel = client.get_channel(997471760029073542)
    embed = discord.Embed(title="Welcome!", description=f"{member.mention} Just Joined")
    await channel.send(embed=embed)

    # Pour envoyer un DM
    await member.send("Welcome!")


# Etape 3
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    pile_ou_face = ['pile', 'face']
    if message.content == 'PoF':
        response = random.choice(pile_ou_face)
        await message.channel.send(response)

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    if message.content == '!help':
        response = 'Commandes possible : 99! , PoF , WhoAreYou '
        await message.channel.send(response)

    if message.content == 'WhoAreYou':
        response = f'{message.author.mention} je suis un bot'
        await message.channel.send(response)


client.run(TOKEN)
