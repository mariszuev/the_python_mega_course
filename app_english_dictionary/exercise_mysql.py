import mysql.connector

con = mysql.connector.connect(
user = "", 
password = "",
host = "",
database = ""
)

cursor = con.cursor()

word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM TABLE WHERE COLUMN = '%s' " % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(results)
else:
    print("Nothing is found!")