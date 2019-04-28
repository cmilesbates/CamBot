import discord

client = discord.Client()

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

try:
    token_file = open("token.txt")
    token = token_file.readline().rstrip("\n\r")
    client.run(token)
except FileNotFoundError:
    print("Please put token in token.txt")
