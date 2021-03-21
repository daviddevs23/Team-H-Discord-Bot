import discord, requests, re, os, random, asyncpraw
from discord.ext import commands

# Grab access info for Reddit API
def tokens(index):
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[index].strip()


# Class for downloading and posting memes
class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Grabs a meme off of the internet and posts it
    @commands.command()
    async def meme(self, ctx):
        reddit = asyncpraw.Reddit(
                client_id=tokens(4),
                client_secret=tokens(5),
                user_agent="TeamHBot"
                )

        # Randomly pick a meme sub
        subs = [
                "memes",
                "dankmemes",
                "antimeme",
                "wholesomememes",
                ]

        sub = await reddit.subreddit(subs[random.randint(0, len(subs) - 1)])

        memes = []
        url = ""
        file_name = ""
        
        # Get rid of pinned posts
        async for post in sub.hot(limit=25):
            if not post.stickied and not post.over_18:
                memes.append(post)

        url = memes[random.randint(0, len(memes) - 1)].url
        file_name = url.split("/")


        if len(file_name) == 0:
            file_name = re.findall("/(.*?)", url)

        file_name = file_name[-1]
        
        # Check if it is an image
        if "." not in file_name:
            file_name += ".jpg"

        r = requests.get(url)

        with open(file_name, "wb") as f:
            f.write(r.content)

        await ctx.send(file=discord.File(file_name))

        os.remove(file_name)



