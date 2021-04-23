import discord
from discord.ext import commands

# Import Commands
from extensions.startup import Startup
from extensions.RNG import RNG
from extensions.admin import Admin
from extensions.meme import Meme
from extensions.dad import Dad
from extensions.poll import Poll
from extensions.music import Music
from extensions.roast import Roast
from extensions.story import Story
from extensions.converse import Converse
from extensions.experience import Experience
from extensions.text import Text


# Command for parcing token.txt
def get_token(index):
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[index].strip()

# Set the command prefix dynamically when initializing bot
client = commands.Bot(command_prefix=get_token(0))

# Add the extensions to the main bot
client.add_cog(Startup(client))
client.add_cog(RNG(client))
client.add_cog(Admin(client))
client.add_cog(Meme(client))
client.add_cog(Dad(client))
client.add_cog(Poll(client))
client.add_cog(Music(client))
client.add_cog(Roast(client))
client.add_cog(Story(client))
client.add_cog(Converse(client))
client.add_cog(Experience(client))
client.add_Cog(Text(client))

if __name__ == "__main__":
    client.run(get_token(1))


