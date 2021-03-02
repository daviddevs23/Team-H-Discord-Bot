import discord
import random
import pickle
import os
from discord.ext import commands
from math import floor


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
        tttarr = [["n","n","n"],["n","n","n"],["n","n","n"]]
        if x == None:
            await ctx.send("The tic tac toe command needs an argument after it, \"Restart\" to start or restart a game")
            return
        elif x == "Restart":
            with open("tictactoe.txt", "wb") as f:
                pickle.dump(tttarr, f)
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
                if tttarr[posx][posy] != "n":
                    await ctx.send("There is already an X or O at that position.")
                    return
                else:
                    tttarr[posx][posy] = "X"
                    if check_tictactoe(tttarr) == 1:
                        await ctx.send("You win!")
                        os.remove("tictactoe.txt")
                        for row in range(3):
                            await ctx.send(tttarr[row][0] + " " + tttarr[row][1] + " " + tttarr[row][2])
                        return
                    compx = 0
                    compy = 0
                    while tttarr[compx][compy] != "n":
                        compx = randomnumgen(3)
                        compy = randomnumgen(3)
                    tttarr[compx][compy] = "O"
                    if check_tictactoe(tttarr) == 1:
                        await ctx.send("I win!")
                        os.remove("tictactoe.txt")
                        for row in range(3):
                            await ctx.send(tttarr[row][0] + " " + tttarr[row][1] + " " + tttarr[row][2])
                        return
                    with open("tictactoe.txt", "wb") as f:
                        pickle.dump(tttarr, f)
                    for row in range(3):
                        await ctx.send(tttarr[row][0]+" "+tttarr[row][1]+" "+tttarr[row][2])
                    return
            await ctx.send("The tic tac toe command needs an argument after it of the form \"0 1\"")
            return
