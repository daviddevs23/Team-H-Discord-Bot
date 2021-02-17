import discord

# A function to grab items from token.txt
def get_token(index):
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[index].strip()


class ShunnedBot(discord.Client):
    # Asynchronous __init__ method
    async def on_ready(self):
        self.deliminator = get_token(0)
        print(self.deliminator)
        print("Bot has been initiated")

    async def on_message(self, message):
        if message.content.find(self.deliminator) == 0:
            await message.channel.send(message.content.replace("::", ""))

if __name__ == "__main__":
    client = ShunnedBot()
    client.run(get_token(1))
