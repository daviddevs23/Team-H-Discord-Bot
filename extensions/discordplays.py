import discord
import os
from discord.ext import commands

import time
import socket

HEADER = 64
PORT    = 17770
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "71.10.216.2"
ADDR    = (SERVER, PORT)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length_padded = send_length + b' '* (HEADER - len(send_length))
    client.send(send_length_padded)
    client.send(message)
    client.send(DISCONNECT_MESSAGE)


class Discordplays(commands.Cog):

    #Initializer function
    def __init__(self, client):
        self.client = client

    #Listener for a single letter to be pressed
    @commands.Cog.listener()
    async def on_message(self, message):

        # Convert message object to an all lowercase string
        content = message.content
        content = content.lower()

        # A really inefficent way of checking to see if a correct character was input
        if 'w'== content:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            send(content)
            return
        elif 'a'== content:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            send(content)
            return
        elif 's'== content:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            send(content)
            return
        elif 'd'== content:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            send(content)
            return
        elif 'j'== content:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            send(content)
            return
        
        elif 'k'== content:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            send(content)
            return
                      
        elif 'n'== content:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            send(content)
            return
        elif 'm'== content:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            send(content)
            return
        elif 'u'== content:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            send(content)
            return
        elif 'i'== content:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            send(content)
            return
