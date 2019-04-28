import discord

client = discord.Client()

token = "PLACE TOKEN HERE"

@client.event
async def on_ready():
    print("CamBot is ready!")
    await client.change_presence(activity=discord.Game("Making a Bot"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!hello"):
        channel = message.channel
        response = "Hi, " + message.author.mention + "!"
        await channel.send(response)

client.run(token)
