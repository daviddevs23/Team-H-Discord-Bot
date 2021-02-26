import discord
import random
from discord.ext import commands
from math import floor


# A function to return a random int between the argument and zero
def randomnumgen(x):
    return random.randrange(2147483647) % x


# A function that acts like a switch case for Rock, Paper, Scissors
def rpsswitch(choice):
    rpsswitcher = {
        0: "Rock",
        1: "Paper",
        2: "Scissors",
    }
    return rpsswitcher.get(choice, "null")


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

    # Plays rock, paper, scissors with the user
    @commands.command()
    async def RPSgame(self, ctx, x=None):
        if x == None:
            await ctx.send("The RPSgame command is for Rock, Paper, Scissors. It requires one of those words after it.")
            return

        listofrps = ["rock", "rocks", "paper", "papers", "scissor", "scissors"]
        z = 5
        for i in range(6):
            if x.lower() == listofrps[i]:
                z = randomnumgen(3)
                await ctx.send(rpsswitch(z))
                i = int(floor(i/2))
                if i == z:
                    await ctx.send("We tied!")
                elif i == 0:
                    if z == 1:
                        await ctx.send("Paper beats rock, I win!")
                    elif z == 2:
                        await ctx.send("Rock beats scissors, you win.")
                elif i == 1:
                    if z == 0:
                        await ctx.send("Paper beats rock, you win.")
                    elif z == 2:
                        await ctx.send("Scissors beats paper, I win!")
                else:
                    if z == 0:
                        await ctx.send("Rock beats scissors, I win!")
                    elif z == 1:
                        await ctx.send("Scissors beats paper, you win.")
                return
        if z == 5:
            await ctx.send("The RPSgame command is for Rock, Paper, Scissors. It requires one of those words after it.")
