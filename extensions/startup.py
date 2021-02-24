import discord
from discord.ext import commands


# Use this for any utilities you need run on start up. Things like
# connecting to a database.
class Startup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot has initialized")

    # Just and example of a cog based command
    @commands.command()
    async def example(self, ctx):
        await ctx.send("Example Commands")
