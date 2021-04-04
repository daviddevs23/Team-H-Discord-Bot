import discord
import os
import asyncpraw
import random
import requests
import re
from discord.ext import commands


# Grab access info for Reddit API
def tokens(self, index):
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[index].strip()


class Story(commands.Cog):

    # intialize client
    def __init__(self, client):
        self.client = client



    # story command
    @commands.command()
    async def story(self, ctx):

        # initialize praw
        reddit = asyncpraw.Reddit(
                            client_id=tokens(self, 2),
                            client_secret=tokens(self, 3),
                            user_agent="TeamHBot"
                            )

        # List of subreddits
        subs =  [
                    "Microfiction",
                    "TwoSentenceHorror",
                    "TwoSentenceComedy"
                ]

        # Choose random subreddit from subs
        sub = await reddit.subreddit(random.choice(subs))
        posts = sub.hot(limit = 50)

        # Empty list to store posts
        stories = []

        # url and filname initialized for embedding
        title = ""
        contents = ""

        # Get rid of pinned posts and append to stories
        async for post in posts:
            if not post.stickied and not post.over_18:
                stories.append(post)

        rand_story = random.choice(stories)

        title = rand_story.title
        contents = rand_story.selftext

        em = discord.Embed(title = title, description = contents)

        await ctx.send(embed = em)


