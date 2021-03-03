import discord
from discord.ext import commands


class Poll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def poll(self, ctx, question, *options: str):
        if len(options) <= 1:
            await ctx.send('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await ctx.send('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['✅', '❌']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']


        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description))
        react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await react_message.edit_message(embed=embed)

    @commands.command(pass_context=True)
    async def tally(self, ctx, id=None):
        poll_message = await ctx.channel.fetch_message(id)
        embed = poll_message.embeds[0]
        unformatted_options = [x.strip() for x in embed.description.split('\n')]
        print(f'unformatted{unformatted_options}')
        opt_dict = {x[:2]: x[3:] for x in unformatted_options} if unformatted_options[0][0] == '1' \
            else {x[:1]: x[2:] for x in unformatted_options}
        # check if we're using numbers for the poll, or x/checkmark, parse accordingly
        voters = [self.client.user.id]  # add the client's ID to the list of voters to exclude it's votes

        tally = {x: 0 for x in opt_dict.keys()}
        for reaction in poll_message.reactions:
            if reaction.emoji in opt_dict.keys():
                reactors = await reaction.users().flatten()
                for reactor in reactors:
                    if reactor.id not in voters:
                        tally[reaction.emoji] += 1
                        voters.append(reactor.id)
        output = f"Results of the poll for '{embed.title}':\n" + '\n'.join(['{}: {}'.format(opt_dict[key], tally[key]) for key in tally.keys()])
        await ctx.send(output)


def setup(client):
    client.add_cog(Poll(client))

'''
import discord, requests, re, os
from discord.ext import commands, tasks





class Poll(commands.Cog):

    # Initializer function
    def __init__(self, client):
        self.client = client

    # Listener to confirm client has booted properly
    @commands.Cog.listener()
    async def on_ready(self):
        print('Polling client is Online')

    
    @commands.Cog.listener()
    async def on_message(self, message):
        # Convert message object to string
        content = message.content
        
        deliminer = content[:2]
        print(type(deliminer))
        if deliminer == '||':
            print(content[3:])
            
            split = content.split()
            
            print(split)


            tf = split.pop(0)
            print(split)

            
            if tf == 'tf':
                await message.channel.send('True or False\n'+ split(0))
            else:
                await message.channel.send('Didnt get a good command')
            
        else:
            return
        '''

	
      




