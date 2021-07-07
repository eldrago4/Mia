import discord
from discord.ext import commands
import requests
from Discord-Emotes import smug, hug, kiss, pat, poke, slap, tickle, neko, ngif, cuddle

smug()
hug()
kiss()
pat()
poke()
slap()
tickle()
neko()
ngif()
cuddle()

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def on_message(message):
    if message.author == client.user:
        return
msg = message.content
m = discord.Embed
     if msg.startswith(';smug')
     smug = Discord-Emotes.smug
     await message.channel.send(smug)