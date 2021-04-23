import discord
from discord.ext import commands
import os
from twilio.rest import Client
from extensions.database import insertUserContact, getUserContact


def tokens(index):
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[index].strip()


def send_message(number, text):
    account_sid = tokens(11)
    auth_token = tokens(12)
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
        member = str(member)
        number = getUserContact(member)

        if not number:
            await ctx.send('Users number is not in database.')
            return

        send_message(number, message)


    @commands.command()
    async def addNumber(self, ctx, number=''):
        user = ctx.author
        user = str(user)
        temp = insertUserContact(user, number)

        if temp:
            await ctx.send('Number added successfully!')
        else:
            await ctx.send('An error occured, try again later.')






