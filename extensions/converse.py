import discord
from discord.ext import commands
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(name='ConverseBot', read_only=False,
                 logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])

intro_talk = ['what is your name?',
              'I\'m ConverseBot, nice to meet you.',
              'blue'
              'That is my old name!']
meme_talk = ['Blobfish',
             'The great blobbed one!',
             'discord',
             'I am a discord Bot.',
             '?',
             'The answer to life, the universe, and everything is 42.']
# Temporary will be replaced by help command description
discord_talk = ['converse',
                'Ask me something.',
                'help',
                'I list the commands you can tell me to do.',
                'coinflip',
                'I flip a coin.',
                'choose',
                'Give me a number, and I will choose a random option between one and that number.',
                'RPSgame',
                'We can play Rock, Paper, Scissors if you choose one of those when asking me.',
                'ttt',
                'We can play Tic-Tac-Toe. First you need to tell me to \"start\" the game,'
                ' then choose a position like this \"0 2\"',
                'hangman',
                'We can play Hangman. First you need to tell to \"start\", then you can start guessing single letters.',
                'meme',
                'I will post a random meme from the subreddits meme, dankmemes, antimeme, or wholesomememes.',
                'clear',
                'As long as you are an Admin, I will clear the last <default 10> messages.',
                'dad',
                'I will tell you a Dad joke.',
                'play',
                'Give the youtube url of a video and I will play it in the General voice channel.',
                'leave',
                'I will leave a voice channel if I am in one.',
                'pause',
                'I will pause the audio, if I am playing something.',
                'resume',
                'I will resume the audio, if I was playing something.',
                'stop',
                'I will stop playing audio.',
                'roast',
                'I will roast you or a user if specified.',
                'story',
                'I will tell you a short story.']
ltrainer = ListTrainer(my_bot)
for phrase in (intro_talk, meme_talk, discord_talk):
    ltrainer.train(phrase)
ctrainer = ChatterBotCorpusTrainer(my_bot)
ctrainer.train('chatterbot.corpus.english')


# Conversation bot
class Converse(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Chats with the bot
    @commands.command(description="Chat with me")
    async def chat(self, ctx, sentence=None):
        if sentence == None:
            await ctx.send("You need to say something.")
        else:
            await ctx.send(my_bot.get_response(sentence.lower()))
