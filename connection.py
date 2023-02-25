import sqlite3

with sqlite3.connect("password_vault.db") as mydb :
    mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE If not exists master(
    Id INTEGER PRIMARY KEY,
    password TEXT not NULL);
    """)

mycursor.execute("""CREATE TABLE If not exists vault(
    Id INTEGER PRIMARY KEY,
    website TEXT not NULL,
    username TEXT not NULL,
    password TEXT not NULL);
    """)