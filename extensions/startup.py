import discord
from discord.ext import commands


# Use this for any utilities you need run on start up. Things like
# connecting to a database.
class Startup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        # Set Bot Status
        # Someone can change the status if they wish
        await self.client.change_presence(status=discord.Status.online, 
                activity=discord.Game("Coding and Stuffs"))

        print("Bot has initialized")

