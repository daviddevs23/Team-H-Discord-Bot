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

def insertUserContact(username, number):
    try:
        basestmt = "insert into userContact values(%s, %s);"
        number = encryptPhrase(number)
        cursor.execute(basestmt, (username, number))
        
        conn.commit()
        return True

    except:
        return False

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
    
