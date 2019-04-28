import discord

client = discord.Client()

valid_commands = ["hello", ":heart: (<3)"]

def display_valid_commands():
    response = "\n**Here is a list of available commands:**"
    for i in range(len(valid_commands)):
        response += "\n*" + str(i+1) + ". " + valid_commands[i] + "*"
    return response

@client.event
async def on_ready():
    print("CamBot is ready!")
    await client.change_presence(activity=discord.Game("Making a Bot"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!cambot"):
        commands = message.content.split(' ')
        channel = message.channel
        print(commands[1])
        if len(commands) == 1:
            response =  message.author.mention + ": **The syntax for this bot is** ***" + commands[0] + " <command>.***"
            response += display_valid_commands()
        elif commands[1] == "hello":
            response = "Hi, " + message.author.mention + "!"
        elif commands[1] == "❤":
            response = "I :heart: you too, " + message.author.mention + "!"
        else:
            response = message.author.mention + ": **This command is invalid!**"
            response += display_valid_commands()

        await channel.send(response)

try:
    token_file = open("token.txt")
    token = token_file.readline().rstrip("\n\r")
    client.run(token)
except FileNotFoundError:
    print("Please put token in token.txt")
