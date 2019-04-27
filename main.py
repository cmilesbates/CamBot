import discord

client = discord.Client()

@client.event
async def on_ready():
    print("CamBot is ready!")
    await client.change_presence(game=discord.Game(name="Making a Bot"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        await client.send_message(message.channel, "World")

if __name__ == "__main__":
    try:
        token_file = open("token.txt", "r")
        token = token_file.readline()
        client.run(token)
    except FileNotFoundError:
        print("Token File not found. Please run again with token stored in token.txt")
