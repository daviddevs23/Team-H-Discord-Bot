import discord
import random
#import os
import requests
import re
from discord.ext import commands
from math import floor
from bs4 import BeautifulSoup
from extensions.database import *

# A function to return a random int between the argument and zero
def randomnumgen(x):
    return random.randrange(2147483647) % x


# A function that acts like a switch case for Rock, Paper, Scissors
def rpsswitch(choice):
    rpsswitcher = {
        0: "Rock",
        1: "Paper",
        2: "Scissors",
    }
    return rpsswitcher.get(choice, "null")


# TicTacToe command needs some more error checking
# Command for checking if tttarr has a player that won
def check_tictactoe(tttarr):
    if tttarr[0][0] == "X" and tttarr[1][1] == "X" and tttarr[2][2] == "X":
        return 1
    elif tttarr[0][0] == "O" and tttarr[1][1] == "O" and tttarr[2][2] == "O":
        return 1
    elif tttarr[0][2] == "X" and tttarr[1][1] == "X" and tttarr[2][0] == "X":
        return 1
    elif tttarr[0][2] == "O" and tttarr[1][1] == "O" and tttarr[2][0] == "O":
        return 1
    j = 0
    while j < 3:
        if tttarr[j][0] == "X" and tttarr[j][1] == "X" and tttarr[j][2] == "X":
            return 1
        elif tttarr[j][0] == "O" and tttarr[j][1] == "O" and tttarr[j][2] == "O":
            return 1
        elif tttarr[0][j] == "X" and tttarr[1][j] == "X" and tttarr[2][j] == "X":
            return 1
        elif tttarr[0][j] == "O" and tttarr[1][j] == "O" and tttarr[2][j] == "O":
            return 1
        j = j + 1
    return 0


# Command for checking if the tictactoe game is in a stalemate
def stale_tictactoe(tttarr):
    for row in range(3):
        for col in range(3):
            if tttarr[row][col] == "- ":
                return 1
    return 0


# Web-scrapes wikipedia for an article title to use for the Hangman game
def hgwebscraper(linknum):
    response = requests.get(url="https://en.wikipedia.org/wiki/Discord_(software)")
    soup = BeautifulSoup(response.content, "html.parser")
    linklist = soup.find(id="bodyContent").find_all("a")
    random.shuffle(linklist)
    link = 0
    for l in linklist:
        if l['href'].find("/wiki/") == -1:
            continue
        link = l
        break
    while linknum > 0:
        link = "https://en.wikipedia.org" + link['href']
        response = requests.get(url=link)
        soup = BeautifulSoup(response.content, "html.parser")
        linklist = soup.find(id="bodyContent").find_all("a")
        random.shuffle(linklist)
        for l in linklist:
            if l['href'].find("/wiki/") == -1:
                continue
            link = l
            break
        linknum -= 1
    return link

# Command to replace non-alpha and space characters for Hangman
def hangman_validator(st):
    validhchars = list("abcdefghijklmnopqrstuvwxyz ")
    for ch in st:
        if ch not in validhchars:
            st = st.replace(ch, " ")
    return re.sub(' +', ' ', st).strip()


# Command to check if Hangman was won
def hgwon(stri):
    for hgc in stri:
        if hgc == "-":
            return 1
    return 0


# Command to create the ascii art for Hangman
def hgart(liv):
    if liv == 5:
        return "___\n|  0"
    elif liv == 4:
        return "___\n|  0\n|  |\n|  |"
    elif liv == 3:
        return "___\n|   0\n| /|\n|   |"
    elif liv == 2:
        return "___\n|   0\n| /|\\\n|   |"
    elif liv == 1:
        return "___\n|   0\n| /|\\\n|   |\n| /"
    elif liv == 0:
        return "___\n|   0\n| /|\\\n|   |\n| /\\"


# Helper method to facilitate transactions
def helperEcoPoints(serverid, username, amount):
    createEconomyBoi(serverid, username)
    if amount >= 0:
        depositPoints(serverid, username, amount)
        return True
    userbal = getPointsBalance(serverid, username)
    if amount < 0:
        amount = abs(amount)
        if amount > userbal:
            return False
        else:
            withdrawPoints(serverid, username, amount)
            return True


# RNG commands test class
class RNG(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Outputs heads or tails in a presumably 50/50 ratio
    @commands.command(description="Command used for flipping a coin")
    async def coinflip(self, ctx):
        if randomnumgen(2) == 1:
            await ctx.send("Heads")
        else:
            await ctx.send("Tails")

    # Takes a positive int argument and outputs a numbered random choice between 1 and the int
    @commands.command(description="Give a number, and I will choose a random option between one and that number")
    async def choose(self, ctx, number=None):
        if number == None:
            await ctx.send("The choose command requires an integer argument greater than 1 after it.")
        elif number.isdigit() and int(number) > 1:
            await ctx.send("Choose option " + str(randomnumgen(int(number)) + 1))
        else:
            await ctx.send("The choose command requires an integer argument greater than 1 after it.")

    # Gives the user's balance
    @commands.command(description="Shows how many points you have in your account.")
    async def account(self, ctx):
        createEconomyBoi(ctx.guild.id, ctx.author)
        x = "You have " + str(getPointsBalance(ctx.guild.id, ctx.author)) + " points."
        await ctx.send(x)

    # Plays rock, paper, scissors with the user
    @commands.command(description="We can play Rock, Paper, Scissors if you choose one of those when asking me")
    async def RPSgame(self, ctx, choice=None):
        if choice == None:
            await ctx.send("The RPSgame command is for Rock, Paper, Scissors. It requires one of those words after it.")
            return

        listofrps = ["rock", "rocks", "paper", "papers", "scissor", "scissors"]
        z = 5
        for i in range(6):
            if choice.lower() == listofrps[i]:
                z = randomnumgen(3)
                await ctx.send(rpsswitch(z))
                i = int(floor(i/2))
                if i == z:
                    await ctx.send("We tied!")
                elif i == 0:
                    if z == 1:
                        helperEcoPoints(ctx.guild.id, ctx.author, -10)
                        await ctx.send("Paper beats rock, I win!")
                    elif z == 2:
                        helperEcoPoints(ctx.guild.id, ctx.author, 10)
                        await ctx.send("Rock beats scissors, you win.")
                elif i == 1:
                    if z == 0:
                        helperEcoPoints(ctx.guild.id, ctx.author, 10)
                        await ctx.send("Paper beats rock, you win.")
                    elif z == 2:
                        helperEcoPoints(ctx.guild.id, ctx.author, -10)
                        await ctx.send("Scissors beats paper, I win!")
                else:
                    if z == 0:
                        helperEcoPoints(ctx.guild.id, ctx.author, -10)
                        await ctx.send("Rock beats scissors, I win!")
                    elif z == 1:
                        helperEcoPoints(ctx.guild.id, ctx.author, 10)
                        await ctx.send("Scissors beats paper, you win.")
                return
        if z == 5:
            await ctx.send("The RPSgame command is for Rock, Paper, Scissors. It requires one of those words after it.")

    # Plays tic-tac-toe
    @commands.command(description="We can play Tic-Tac-Toe. First tell me to \"start\" the game, then choose a coord")
    async def ttt(self, ctx, x=None, y=None):
        tttarr = [["- ","- ","- "],["- ","- ","- "],["- ","- ","- "]]
        if x == None:
            await ctx.send("The tic tac toe command needs an argument after it, \"Restart\" to start or restart a game")
            return
        elif x == "Restart" or x == "restart" or x == "Start" or x == "start":
            if tttCreateGame(ctx.guild.id, tttarr):
                await ctx.send("Reset game.")
            else:
                await ctx.send("Sorry, failed to create a tic-tac-toe game for this server.")
            return
        else:
            if x.isdigit() and y.isdigit() and 3 > int(x) >= 0 and 3 > int(y) >= 0:
                posx = int(y)
                posy = int(x)
                tttarr = tttGetCurrentBoard(ctx.guild.id)
                if not tttarr:
                    await ctx.send("You must \"Start\" the game first to play.")
                    return
                if tttarr[posx][posy] == "O" or tttarr[posx][posy] == "X":
                    await ctx.send("There is already an X or O at that position.")
                    return
                else:
                    tttarr[posx][posy] = "X"
                    if check_tictactoe(tttarr) == 1:
                        helperEcoPoints(ctx.guild.id, ctx.author, 30)
                        await ctx.send("You win!")
                        tttDeleteGame(ctx.guild.id)
                        for row in range(3):
                            await ctx.send(tttarr[row][0] + "  " + tttarr[row][1] + "  " + tttarr[row][2])
                        return
                    if stale_tictactoe(tttarr) == 0:
                        await ctx.send("We are in a stalemate.")
                        tttDeleteGame(ctx.guild.id)
                        for row in range(3):
                            await ctx.send(tttarr[row][0] + "  " + tttarr[row][1] + "  " + tttarr[row][2])
                        return
                    compx = 0
                    compy = 0
                    while tttarr[compx][compy] == "O" or tttarr[compx][compy] == "X":
                        compx = randomnumgen(3)
                        compy = randomnumgen(3)
                    tttarr[compx][compy] = "O"
                    if check_tictactoe(tttarr) == 1:
                        helperEcoPoints(ctx.guild.id, ctx.author, -30)
                        await ctx.send("I win!")
                        tttDeleteGame(ctx.guild.id)
                        for row in range(3):
                            await ctx.send(tttarr[row][0] + "  " + tttarr[row][1] + "  " + tttarr[row][2])
                        return
                    if not tttUpdateGame(ctx.guild.id, tttarr):
                        await ctx.send("Failed to save the turn.")
                        return
                    for row in range(3):
                        await ctx.send(tttarr[row][0]+"  "+tttarr[row][1]+"  "+tttarr[row][2])
                    return
            await ctx.send("The tic tac toe command needs an argument after it of the form \"0 1\"")
            return

    # Plays hangman
    @commands.command(description="We can play Hangman. First you need to tell to \"start\", then you can start "
                                  "guessing individual letters")
    async def hangman(self, ctx, letter=None):
        text = ''
        hgame = hangmanGetCurrentGame(ctx.guild.id)
        if letter == None:   # No argument provided
            await ctx.send("The hangman command needs an argument, \"Restart\" to restart a game, a letter to guess")
            return
        elif letter == "Restart" or letter == "restart" or letter == "Start" or letter == "start":  # Restarts the game
            successLink = 0
            while successLink == 0:
                try:
                    link = hgwebscraper(2)  # Grabs a random wikipedia article link
                    successLink = 1
                except:
                    successLink = 0
            print(link)
            text = link['title'].lower()
            text = hangman_validator(text)  # Formats word/phrase for hangman
            blankstr = ""
            for ch in text:     # Replaces the letters with dashes in the string shown to players
                if ch == " ":
                    blankstr += " "
                else:
                    blankstr += "-"
            hangmanCreate(ctx.guild.id, text, blankstr)
            await ctx.send("Reset game.")
            return
        elif not hgame:  # Requires that the game is 'started' for each server
            await ctx.send("You must \"Restart\" the game first to play.")
            return
        elif letter.isalpha() and len(letter) == 1:       # Checks that the argument is a single letter
            correct = 1
            oristr = hgame[1]
            guestr = hgame[0]
            guessedchars = hangmanGuessedWrongLetters(ctx.guild.id)     # Grabs used letters from the server
            i = 0
            x = letter.lower()
            if guessedchars.find(x) != -1:
                await ctx.send("That letter was already guessed.")
                return
            hangmanUpdateWrongGuessed(ctx.guild.id, x)
            while i < len(oristr):      # loops through the original string
                if oristr[i] == x:
                    correct = 0         # indicates chosen letter is in the string
                    guestr = guestr[:i] + x + guestr[i+1:]  # sets the char to the same position in the guessed string
                i += 1
            if correct == 0:            # outputs and updates text file for correct guesses
                await ctx.send("Correct!")
                await ctx.send(guestr)
                if hgwon(guestr) == 0:
                    hangmanDelete(ctx.guild.id)     # Deletes the game from the server if it was won
                    helperEcoPoints(ctx.guild.id, ctx.author, 30)
                    await ctx.send("The person was saved, you won!")
                    return
                hangmanUpdate(ctx.guild.id, guestr)
                return
            else:                       # outputs and updates text file for incorrect guesses
                await ctx.send("Wrong!")
                lives = hangmanGetLives(ctx.guild.id)
                outstr = hgart(lives)    # gets ascii art for the number of lives remaining
                await ctx.send(outstr)
                if lives == 0:
                    hangmanDelete(ctx.guild.id)     # Deletes the game from the server if it was lost
                    endstr = "It was \"" + oristr + "\"."
                    await ctx.send("The person was hung, you lost!")
                    await ctx.send(endstr)
                    helperEcoPoints(ctx.guild.id, ctx.author, -30)
                    return
                decrementHangmanLives(ctx.guild.id)
                return
        else:           # no argument was provided
            await ctx.send("The hangman command needs an argument, \"Restart\" to restart a game, a letter to guess")
            return
