import discord
from discord.ext import commands
import os
from twilio.rest import Client
from database import insertUserContact
from database import getUserContact


def tokens(self, index):
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[index].strip()


def send_message(number, text):
    account_sid = 'AC6a2459ffeba9b76a67e3896c08b6e561' #tokens(self, 12)
    auth_token = 'a93016a605fea7cac23f35f7c64f4a8f' #tokens(self, 13)
    client = Client(account_sid, auth_token)

    client.messages \
        .create(
             body=text,
             from_='+15128723137',
             to= '+1' + number
         )


class Text(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def text(self, ctx, member: discord.Member, message=''):
        number = getUserContact(str(member))
        if not number:
            ctx.send('Users number is not in database.')
            return

        open(f'{member}-text.txt')

        send_message(number, message)


    @commands.command()
    async def addNumber(self, ctx, number=''):
        user = ctx.author
        if insertUserContact(str(user),str(number)):
            await ctx.send('Number added successfully!')
        else:
            await ctx.send('An error occured, try again later.')






