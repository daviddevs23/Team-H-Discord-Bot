import mysql.connector, base64
from cryptography.fernet import Fernet

def get_token(index):
    with open("../token.txt", "r") as f:
        lines = f.readlines()
        return lines[index].strip()

conn = mysql.connector.connect(user=get_token(6),
                               password=get_token(7),
                               host=get_token(8),
                               database=get_token(9))
cursor = conn.cursor(prepared=True)

# An encryption library that encrypts things twice
f = Fernet(base64.urlsafe_b64encode(get_token(10).encode()))

# Convert the message into a encrypted string and returns it
def encryptPhrase(message):
    return f.encrypt(message.encode()).decode()

# Returns the encrypted message as a string and returns the decrypted message
def decryptPhrase(message):
    return f.decrypt(message.encode()).decode()

# Adds in a new user and returns true if it was successful, else it return false
def insertUserContact(username, number):
    try:
        basestmt = "insert into userContact values(%s, %s);"
        number = encryptPhrase(number)
        cursor.execute(basestmt, (username, number))
        
        conn.commit()
        return True

    except:
        return False

# Returns false if there is no user with that username, if it exists, then it
# returns the users number
def getUserContact(username):
    try:
        basestmt = "select number from userContact where name=%s;"
        cursor.execute(basestmt, (username,))

        retVals = []

        for person in cursor:
            retVals.append(person)

        retVals = retVals[0][0]

        retVals = decryptPhrase(retVals)

        return retVals

    except:
        return False
    
# Takes in a serverID and a 2D array for the gameboard
def tttCreateGame(serverID, gameBoard):
    try: 
        tttDeleteGame(serverID)

        basestmt = "insert into ttt values(%s, %s);"
        board = ""
        for i in gameBoard:
            for j in i:
                board = board + j
        
        serverID = str(serverID)

        cursor.execute(basestmt, (str(serverID), board,))
        
        conn.commit()

        return True

    except:
        return False

# Deletes the game with the given serverID. If it succeeds, it returns True, else
# false
def tttDeleteGame(serverID):
    try:
        basestmt = "delete from ttt where serverID=%s;"

        cursor.execute(basestmt, (serverID,))
        conn.commit()

        return True

    except:
        return False

# Updates the gameboard of the given server. If it succeeds, it returns True,
# else it returns False
def tttUpdateGame(serverID, gameBoard):
    try:
        basestmt = "update ttt set board=%s where serverID=%s;"

        board = ""
        for i in gameBoard:
            for j in i:
                board = board + j

        cursor.execute(basestmt,(board, serverID,))
        conn.commit()
        
        return True

    except:
        return False

 # Returns a 2d array of the game if it exists, if a game with that ID does not
 # exist, it will return false. Can be used to check if a game exists
def tttGetCurrentBoard(serverID):
    try:
        basestmt = "select board from ttt where serverID=%s;"
        
        cursor.execute(basestmt, (serverID,))
        res = []

        for i in cursor:
            res.append(i)

        if len(res[0]) == 0:
            return False

        res = list(res[0][0].replace(" ", ""))

        for i in range(len(res)):
            if res[i] == "-":
                res[i] = "- "

        return [res[0:3], res[3:6], res[6:9]]

    except:
        return False

# Pass in the serverID, desired word, and the currentWord. For the currentWord,
# you could probably just pass it in with the underscores and spacing.
def hangmanCreate(serverID, correctWord, currentWord):
    try: 
        hangmanDelete(serverID)

        basestmt = "insert into hangman values(%s, %s, %s);"

        cursor.execute(basestmt, (serverID, currentWord, correctWord))
        
        conn.commit()

        return True

    except:
        return False

# Just enter the serverID and the current state of the word they are guessing
def hangmanUpdate(serverID, currentWord):
    try:
        basestmt = "update hangman set currentGuess=%s where serverID=%s;"

        cursor.execute(basestmt,(currentWord, serverID,))
        conn.commit()
        
        return True

    except:
        return False

# Returns a tuple of (currentWord, correctWord). If it doesn't exist, it returns
# False
def hangmanGetCurrentGame(serverID):
    try:
        basestmt = "select currentGuess, correctGuess from hangman where serverID=%s;"
        
        cursor.execute(basestmt, (serverID,))
        res = []

        for i in cursor:
            res.append(i)

        if len(res[0]) == 0:
            return False

        return list(res[0])


    except:
        return False

# A helper function that returns the current string of guessed wrong letters, else False
def hangmanGuessedWrongLetters(serverID):
    try:
        basestmt = "select guessed from hangman where serverID=%s;"

        cursor.execute(basestmt,(serverID,))
        res = []

        for i in cursor:
            res.append(i)

        if len(res[0]) == 0:
            return False

        return res[0][0]

    except:
        return False

# Gets you the number of lives you have left, if it fails, it will return False
def hangmanGetLives(serverID):
    lives = 5

    try:
        return lives - len(hangmanGuessedWrongLetters(serverID))

    except:
        return False

# Adds the specified letter to the guessed letter string. It will return the 
# string of guessed letters if it was successful, else False
def hangmanUpdateWrongGuessed(serverID, letter):
    try:

        letter = letter.lower()
        guessed = hangmanGuessedWrongLetters(serverID)

        if (letter not in guessed):
            guessed = guessed + letter

            basestmt = "update hangman set guessed=%s where serverID=%s;"
            cursor.execute(basestmt, (guessed, serverID))

            conn.commit()

        return guessed

    except:
        return False

# Deletes the game of the given serverID
def hangmanDelete(serverID):
    try:
        basestmt = "delete from hangman where serverID=%s;"

        cursor.execute(basestmt, (serverID,))
        conn.commit()

        return True

    except:
        return False

print(hangmanUpdateWrongGuessed("Test", "H"))
