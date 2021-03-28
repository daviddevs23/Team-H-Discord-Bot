import discord
from discord.ext import commands


# A command class for adding and removing members and other admin level commands
class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Kick member
    @commands.command(description="Admin command used for removing individuals")
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
    @commands.command(description="Admin command used to permantly remove individuals")
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
    @commands.command(description="Admin command that allows a user to rejoin")
    async def unban(self, ctx, *, member=None):
        # Check if the person sending the command is an admin
        if ctx.author.guild_permissions.administrator:

            # Make sure a member was actually passed in
            if member != None:
                banned_members = await ctx.guild.bans()
                member_name, member_id = member.split("#")

                unbanned = False

                for member in banned_members:
                    user = member.user

                    if (user.name, user.discriminator) == (member_name, member_id):
                        unbanned = True

                        await ctx.guild.unban(user)
                        await ctx.send(f"Unbanned {user.name}#{user.discriminator}")

                if not unbanned:
                    ctx.send(f"Unable to find member to unban")

            else:
                await ctx.send("Please provide a member to unban")

        else:
            await ctx.send(f"Sorry, you are not an admin {ctx.author}")

    # Simple clear messages utility
    @commands.command()
    async def clear(self, ctx, num_messages=10):
        # Make sure person calling command is an admin
        if ctx.author.guild_permissions.administrator:
            await ctx.channel.purge(limit=num_messages)

        else:
            await ctx.send("Sorry, you are not an administrator")

