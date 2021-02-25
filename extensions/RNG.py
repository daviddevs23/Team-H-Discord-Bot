import discord
import random
from discord.ext import commands


# A function to return a random int between the argument and zero
def randomnumgen(x):
    return random.randrange(2147483647) % x


# RNG commands test class
class RNG(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Outputs heads or tails in a presumably 50/50 ratio
    @commands.command()
    async def coinflip(self, ctx):
        if randomnumgen(2) == 1:
            await ctx.send("Heads")
        else:
            await ctx.send("Tails")

    # Takes a positive int argument and outputs a numbered random choice between 1 and the int
    @commands.command()
    async def RNG(self, ctx, x=None):
        if x == None:
            await ctx.send("The RNG command requires an integer argument greater than 1 after it.")
        elif x.isdigit() and int(x) > 1:
            await ctx.send("Choose option " + str(randomnumgen(int(x)) + 1))
        else:
            await ctx.send("The RNG command requires an integer argument greater than 1 after it.")

