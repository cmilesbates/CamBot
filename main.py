import discord
import asyncio

from discord.ext import commands

#client = discord.Client()
client = commands.Bot(command_prefix = '!cambot ')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Making a Bot"))

@client.command()
async def hello(ctx):
    response = "Hi, " + ctx.author.mention + "!"
    await ctx.send(response)

#HEART COMMANDS
@client.command(name="<3")
async def _heart1(ctx):
    response = "I :heart: you too, " + ctx.author.mention + "!"
    await ctx.send(response)

@client.command(name=":heart:")
async def _heart2(ctx):
    response = "I :heart: you too, " + ctx.author.mention + "!"
    await ctx.send(response)

@client.command(name="❤")
async def _heart3(ctx):
    response = "I :heart: you too, " + ctx.author.mention + "!"
    await ctx.send(response)

try:
    token_file = open("token.txt")
    token = token_file.readline().rstrip("\n\r")
    client.run(token)
except FileNotFoundError:
    print("Please put token in token.txt")
