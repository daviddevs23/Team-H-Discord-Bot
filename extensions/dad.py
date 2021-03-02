import discord
import os
import random
from discord.ext import commands

#   dad.py is a cog class which holds two functions, one to check messages for "I'm"
#   and another that sends a dad joke when .dad command is called

class Dad(commands.Cog):

    # Initializer function
    def __init__(self, client):
        self.client = client

    # Listener to confirm bot has booted properly
    @commands.Cog.listener()
    async def on_ready(self):
        print('Dad Bot is online.')

    # Listener that checks messages for "I'm"
    @commands.Cog.listener()
    async def on_message(self, message):

        # Convert message object to string
        content = message.content

        # Check if message was sent by dad.py, ignore if it was
        if 'Dad Bot' in content:
            return

        # Check if message contains keyword "I'm"
        if 'I\'m' in content:

            # Split string after "I'm"
            aftIm = content.split("I'm ", 1)[1]

            # Formatted response
            response = f'Hi {aftIm.capitalize()}, I\'m Dad Bot!'

            # send message to channel
            await message.channel.send(response)
            return

    # Command for dad joke
    @commands.command()
    async def dad(self, ctx):

        # List of dad jokes
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
                    'I told my girlfriend she drew her eyebrows too high. She seemed surprised.',
                    'I bought my friend an elephant for his room. He said \"Thanks\". I said \"Don\'t mention it\".',
                    'I poured root beer in a square glass. Now I just have beer',
                    'I have an EpiPen. My friend gave it to me when he was dying. It seemed very important to him that I have it.',
                    'So what if I don\'t want to know what Armageddon means? It\'s not the end of the world.',
                    'This is my step ladder. I never knew my real ladder.',
                    'I bought the world\'s worst thesaurus yesterday. Not only is it terrible, it\'s terrible.',
                    'I have the heart of a lion and a lifetime ban from the Toronto zoo.'
                    ]
        # Return random dad joke from list
        await ctx.send(f'{random.choice(dadJokes)}')
