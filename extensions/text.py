import discord
from discord.ext import commands
import os
import smtplib
from smtplib import SMTP


providers = [
                'att-@txt.att.net',
                'tmobile-@tmomail.net',
                'verizon-@vtext.com',
                'sprint-@messaging.sprintpcs.com',
                'uscellular-@email.uscc.net'
            ]

def send_message(user_provider, number, message):
    for prov in providers:
        if user_provider.lower() in prov:
            provider_found = True
            split_provider = prov.split('-')
            extention = split_provider[1]
            send = str(number) + extention

    if not provider_found:
        return 'Provider Not Found'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login( 'teamhsmsbot@gmail.com', 'teamH2021')
    server.sendmail( 'User', send, message)

    return f'Message sent to {number}'

@commands.command()
async def text(self, ctx, user_provider='', number='', message=''):
    if user_provider=='' or number == '' or message=='':
        await ctx.send('To use text, include the users provider, number, and message') 
    else:
        await ctx.send(send_message(user_provider, number, message))







