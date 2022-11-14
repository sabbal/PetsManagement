import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="Petsmanagement"
)
cursorObject = dataBase.cursor()
sql = "INSERT INTO Cats (Cat_id,Name, Breed) VALUES (%s,%s,%s)"
val = [("001", "MIMI","Persian"),
       ("002", "OOlu","Persian"),
       ("003", "Nora","Persian"),
       ("004", "Pumpkin","Persian")]

cursorObject.executemany(sql, val)
dataBase.commit()

print(cursorObject.rowcount, "details inserted"),

dataBase.close(),


