import discord
from discord.ext import commands

# Import Commands
from extensions.startup import Startup

# Command for parcing token.txt
def get_token(index):
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[index].strip()

# Set the command prefix dynamically when initializing bot
client = commands.Bot(command_prefix=get_token(0))

# Add the extensions to the main bot
client.add_cog(Startup(client))

client.run(get_token(1))

