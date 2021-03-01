import discord
from discord.ext import commands


# A command class for adding and removing members
class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Kick member
    @commands.command()
    async def kick(self, ctx, member : discord.Member=None, *, reason=None):
        # Check if the person sending the command is an admin
        if ctx.author.guild_permissions.administrator:

            # Make sure a member was actually passed in
            if member != None:

                # Check to make sure we are not kicking a server admin
                if not member.guild_permissions.administrator:
                    await member.kick(reason=reason)
                    await ctx.send(f"{member} has been kicked")

                else:
                    await ctx.send("Sorry, I do not have permission to kick an admin")

            else:
                await ctx.send("Please provide a member to kick")

        else:
            await ctx.send(f"Sorry, you are not an admin {ctx.author}")

    # Ban member
    @commands.command()
    async def ban(self, ctx, member : discord.Member=None, *, reason=None):
        # Check if the person sending the command is an admin
        if ctx.author.guild_permissions.administrator:

            # Make sure a member was actually passed in
            if member != None:

                # Check to make sure we are not banning a server admin
                if not member.guild_permissions.administrator:
                    await member.ban(reason=reason)
                    await ctx.send(f"{member} has been banned")

                else:
                    await ctx.send("Sorry, I do not have permission to ban an admin")

            else:
                await ctx.send("Please provide a member to ban")

        else:
            await ctx.send(f"Sorry, you are not an admin {ctx.author}")

    # Unban a member
    @commands.command()
    async def unban(self):
        pass


