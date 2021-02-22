import discord

# A function to grab items from token.txt
def get_token(index):
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[index].strip()

client = discord.Client()

TOKEN = get_token(1)
DELIMIN = get_token(0)

@client.event
async def on_ready():
    print(f'Bot {client.user} is now online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f'{DELIMIN}hello'):
        name = str(message.author)
        name = name.split('#')[0]
        await message.channel.send(f'Hello {name}')

    elif message.content.startswith(f'{DELIMIN}test'):
        await message.channel.send('TEST TEST TEST')
    
    elif message.content.startswith(f'{DELIMIN}test2'):
        await message.channel.send('TEST2 TEST2 TEST2')

    ## Add commands here

@client.event
async def on_member_join(member):
    await member.send('Private message')

client.run(TOKEN)
