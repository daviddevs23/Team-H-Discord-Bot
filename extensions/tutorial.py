import discord
import os
from os import path
from discord.ext import commands

def tutorialLine(self, index):
    with open("tutorial.txt", "r") as full_tutorial:
        tutorial_list = []
        i = 0
        for l in full_tutorial.readlines():
            if (i % 2 == 0):
                tutorial_list.append(l)
            i+=1
    return tutorial_list[index].strip()

def endTutorial(self, filename):
    os.remove(filename)


class Tutorial(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def tutorial(self, ctx):
        user = ctx.author
        filename = f'{user}-tutorial.txt'

        if path.isfile(filename):
            await user.send('You already started a tutorial. To reset enter ./resetTutorial')
        else:
            await user.send(tutorialLine(self, 0))

            file = open(f"{filename}", "w")

            file.write("1")
            file.close()


    @commands.command()
    async def resetTutorial(self, ctx):
        user = ctx.author
        filename = f'{user}-tutorial.txt'

        if path.isfile(filename):
            os.remove(filename)
        
        if not path.isfile(filename):
            await user.send('Tutorial reset')

    
    @commands.command()
    async def cont(self, ctx, end_message=''):
        if (path.isfile(f'{ctx.author}-tutorial.txt')) and not ctx.guild:
            user = ctx.author
            filename = f'{user}-tutorial.txt'

            

            if (end_message == 'end'):
                await user.send('Okay, tutorial has been ended')
                endTutorial(self, filename)
                return

            file = open(filename, "r")
            index = int(file.read())
            file.close()

            if index >= 14:
                endTutorial(self, filename)
                return

            next_message = tutorialLine(self, index)
            index +=1

            await user.send(next_message)

            update_file = open(f'{filename}', "w")
            update_file.write(f'{index}')
            update_file.close()



    








