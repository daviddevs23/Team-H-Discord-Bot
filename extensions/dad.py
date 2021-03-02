import discord
import random
from discord.ext import commands

class Dad(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command()
    async def dad(self, ctx):
        dadJokes = ['What do you call a Mexican who lost his car? Carlos.',
                    'What do you call a fake noodle? An Impasta.',
                    'People say they pick their nose, but I feel like I was born with mine.',
                    'Want to hear a joke about paper? Nevermind its tearable',
                    'Did you hear about the restaurant on the moon? Great food, no atmosphere.',
                    'This graveyard looks overcrowded. People must be dying to get in there.',
                    'How many apples grow on a tree? All of them. ',
                    'How can you tell if a ant is a boy or a girl? They’re all girls, otherwise they’d be uncles.',
                    'I asked my friend to help me with a math problem. He said: “Don’t worry; this is a piece of cake.” I said: “No, it’s a math problem."',
                    'I keep trying to lose weight, but it keeps finding me.',
                    'I don’t play soccer because I enjoy the sport. Im just doing it for kicks.',
                    'I used to work in a shoe recycling shop. It was sole destroying.',
                    'Why do you never see elephants hiding in trees? Because they’re so good at it.',
                    'Where did the one-legged waitress work? IHOP!',
                    'How do you organize a space party? You planet.',
                    'A man woke up in a hospital after a serious accident. He shouted, Doctor, doctor, I can’t feel my legs!” The doctor replied, “I know you can’t I’ve cut off your arms!”',
                    'Why do crabs never give to charity? Because they’re shellfish.',
                    'What do you call a fish with no eyes? A fshhhh.',
                    'What do you call a man with no arms and no legs lying in front of your door? Matt.',
                    
                    ]
        await ctx.send(f'{random.choice(dadJokes)}')

