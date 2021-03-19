import discord
import random
import pickle
import os
import requests
import re
from discord.ext import commands
from math import floor
from bs4 import BeautifulSoup


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


# RNG commands test class
class RNG(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Outputs heads or tails in a presumably 50/50 ratio
    @commands.command()
    async def coinflip(self, ctx):
        if randomnumgen(2) == 1:
            await ctx.send("Heads")
        else:
            await ctx.send("Tails")

    # Takes a positive int argument and outputs a numbered random choice between 1 and the int
    @commands.command()
    async def RNG(self, ctx, x=None):
        if x == None:
            await ctx.send("The RNG command requires an integer argument greater than 1 after it.")
        elif x.isdigit() and int(x) > 1:
            await ctx.send("Choose option " + str(randomnumgen(int(x)) + 1))
        else:
            await ctx.send("The RNG command requires an integer argument greater than 1 after it.")

    # Plays rock, paper, scissors with the user
    @commands.command()
    async def RPSgame(self, ctx, x=None):
        if x == None:
            await ctx.send("The RPSgame command is for Rock, Paper, Scissors. It requires one of those words after it.")
            return

        listofrps = ["rock", "rocks", "paper", "papers", "scissor", "scissors"]
        z = 5
        for i in range(6):
            if x.lower() == listofrps[i]:
                z = randomnumgen(3)
                await ctx.send(rpsswitch(z))
                i = int(floor(i/2))
                if i == z:
                    await ctx.send("We tied!")
                elif i == 0:
                    if z == 1:
                        await ctx.send("Paper beats rock, I win!")
                    elif z == 2:
                        await ctx.send("Rock beats scissors, you win.")
                elif i == 1:
                    if z == 0:
                        await ctx.send("Paper beats rock, you win.")
                    elif z == 2:
                        await ctx.send("Scissors beats paper, I win!")
                else:
                    if z == 0:
                        await ctx.send("Rock beats scissors, I win!")
                    elif z == 1:
                        await ctx.send("Scissors beats paper, you win.")
                return
        if z == 5:
            await ctx.send("The RPSgame command is for Rock, Paper, Scissors. It requires one of those words after it.")

    # Plays tic-tac-toe
    @commands.command()
    async def ttt(self, ctx, x=None, y=None):
        tttarr = [["- ","- ","- "],["- ","- ","- "],["- ","- ","- "]]
        if x == None:
            await ctx.send("The tic tac toe command needs an argument after it, \"Restart\" to start or restart a game")
            return
        elif x == "Restart" or x == "restart" or x == "Start" or x == "start":
            with open("tictactoe.txt", "wb") as f:
                pickle.dump(tttarr, f)
                f.close()
            await ctx.send("Reset game.")
            return
        elif not os.path.exists("tictactoe.txt"):
            await ctx.send("You must \"Restart\" the game first to play.")
            return
        else:
            if x.isdigit() and y.isdigit() and 3 > int(x) >= 0 and 3 > int(y) >= 0:
                posx = int(y)
                posy = int(x)
                with open("tictactoe.txt", "rb") as f:
                    tttarr = pickle.load(f)
                    f.close()
                if tttarr[posx][posy] != "- ":
                    await ctx.send("There is already an X or O at that position.")
                    return
                else:
                    tttarr[posx][posy] = "X"
                    if check_tictactoe(tttarr) == 1:
                        await ctx.send("You win!")
                        os.remove("tictactoe.txt")
                        for row in range(3):
                            await ctx.send(tttarr[row][0] + "  " + tttarr[row][1] + "  " + tttarr[row][2])
                        return
                    if stale_tictactoe(tttarr) == 0:
                        await ctx.send("We are in a stalemate.")
                        os.remove("tictactoe.txt")
                        for row in range(3):
                            await ctx.send(tttarr[row][0] + "  " + tttarr[row][1] + "  " + tttarr[row][2])
                        return
                    compx = 0
                    compy = 0
                    while tttarr[compx][compy] != "- ":
                        compx = randomnumgen(3)
                        compy = randomnumgen(3)
                    tttarr[compx][compy] = "O"
                    if check_tictactoe(tttarr) == 1:
                        await ctx.send("I win!")
                        os.remove("tictactoe.txt")
                        for row in range(3):
                            await ctx.send(tttarr[row][0] + "  " + tttarr[row][1] + "  " + tttarr[row][2])
                        return
                    with open("tictactoe.txt", "wb") as f:
                        pickle.dump(tttarr, f)
                        f.close()
                    for row in range(3):
                        await ctx.send(tttarr[row][0]+"  "+tttarr[row][1]+"  "+tttarr[row][2])
                    return
            await ctx.send("The tic tac toe command needs an argument after it of the form \"0 1\"")
            return

    # Plays hangman
    @commands.command()
    async def hangman(self, ctx, x=None):
        text = ''
        if x == None:   # No argument provided
            await ctx.send("The hangman command needs an argument, \"Restart\" to restart a game, a letter to guess")
            return
        elif x == "Restart" or x == "restart" or x == "Start" or x == "start":  # Restarts the game
            link = hgwebscraper(2)  # Grabs a random wikipedia article link
            print(link)
            text = link['title'].lower()
            text = hangman_validator(text)  # Formats word/phrase for hangman
            with open("hangman.txt", "w") as f:  # Sets up hangman.txt into its starting state
                f.write(text)
                f.write("\n6\n")
                for ch in text:
                    if ch == " ":
                        f.write(" ")
                    else:
                        f.write("-")
                f.write("\n ")
                f.close()
            await ctx.send("Reset game.")
            with open("hangman.txt", "r") as f:  # Outputs the blank word/phrase
                lines = f.readlines()
                await ctx.send(lines[2])
                f.close()
            return
        elif not os.path.exists("hangman.txt"):  # Requires that the game is 'started' for other arguments to be checked
            await ctx.send("You must \"Restart\" the game first to play.")
            return
        elif x.isalpha() and len(x) == 1:       # Checks that the argument is a single letter
            correct = 1
            with open("hangman.txt", "r") as f:  # gets the current game state
                lines = f.readlines()
                f.close()
            oristr = list(lines[0])
            guestr = list(lines[2])
            guessedchars = lines[3]
            i = 0
            x = x.lower()
            if guessedchars.find(x) != -1:
                await ctx.send("That letter was already guessed.")
                return
            guessedchars += x
            while i < len(oristr):      # loops through the original string
                if oristr[i] == x:
                    correct = 0         # indicates chosen letter is in the string
                    guestr[i] = x       # sets the character to the same position in the guessed string
                i += 1
            if correct == 0:            # outputs and updates text file for correct guesses
                await ctx.send("Correct!")
                outstr = ""
                for char in guestr:
                    outstr += char
                await ctx.send(outstr)
                if hgwon(outstr) == 0:
                    os.remove("hangman.txt")
                    await ctx.send("The person was saved, you won!")
                    return
                #outstr += "\n"
                lines[2] = outstr
                lines[3] = guessedchars
                with open("hangman.txt", "w") as f:
                    f.writelines(lines)
                    f.close()
                return
            else:                       # outputs and updates text file for incorrect guesses
                await ctx.send("Wrong!")
                lives = int(lines[1])
                lives -= 1
                outstr = hgart(lives)    # gets ascii art for the number of lives remaining
                await ctx.send(outstr)
                if lives == 0:
                    os.remove("hangman.txt")
                    await ctx.send("The person was hanged, you lost!")
                    return
                lines[1] = str(lives) + "\n"
                lines[3] = guessedchars
                with open("hangman.txt", "w") as f:
                    f.writelines(lines)
                    f.close()
                return
        else:           # no argument was provided
            await ctx.send("The hangman command needs an argument, \"Restart\" to restart a game, a letter to guess")
            return
