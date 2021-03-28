import mysql.connector

def get_token(index):
    with open("../token.txt", "r") as f:
        lines = f.readlines()
        return lines[index].strip()

conn = mysql.connector.connect(user=get_token(6),
                               password=get_token(7),
                               host=get_token(8),
                               database=get_token(9))

cursor = conn.cursor(prepared=True)

# Simple example of inserting data. Same process for updating
def exampleInsertion(name, ID):
    try:
        # Use a %s whereever you want to insert data, this protects from
        # SQL injection attacks
        basestmt = 'insert into test values (%s, %s)'
        cursor.execute(basestmt, (name, ID,))
        conn.commit()
        return True
    
    except:
        return False

# Simple example of reading data.
def exampleSelection(name, ID):
    try:
        basestmt = 'select * from test where name=%s and numberID=%s'
        cursor.execute(basestmt,(name, ID,))
        returnVals = []

        # Cursor object stores all of the return values, have to manually
        # grab throught iteration
        for person in cursor:
            returnVals.append(person)

        return returnVals
    
    except:
        return False


