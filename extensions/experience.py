import discord
from discord.ext import commands
from extensions.database import createExperienceBoi, getExperience, incrementExperience

class Experience(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.levels = { "1": "Joker",
                        "2": "2",
                        "3": "3",
                        "4": "4",
                        "5": "5",
                        "6": "6",
                        "7": "7",
                        "8": "8",
                        "9": "9",
                        "10": "10",
                        "11": "Jack",
                        "12": "Queen",
                        "13": "King",
                        "14": "God"}

    @commands.Cog.listener()
    async def on_message(self, ctx):
        incrementAmount = 1

        if ctx.author.id == self.client.user.id:
            return 

        if ctx == None:
            return

        username = ctx.author
        serverID = ctx.guild.id

        experience = getExperience(serverID, username)

        # If user exists, just increment and check for level changes
        if type(experience) == int:
            incrementExperience(serverID, username, incrementAmount)

        # If they don't exist, create user, welcome them, and increment initial values
        else:
            createExperienceBoi(serverID, username)
            incrementExperience(serverID, username, incrementAmount)

        # Get updated value for level checking
        experience = getExperience(serverID, username)

        # Each level takes 100 points
        if experience % 100 == 0:
            if experience / 100 > 14:
                pass

            elif experience / 100 > 0:
                temp = self.levels[str(int(experience/100))]
                await ctx.channel.send(f"Congratulations {username.name}, you have leveled up to {temp}")
