import sqlite3

con=sqlite3.connect("data.db")
cursor=con.cursor()
create_table="CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table_item="CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY,name text, price real)"
cursor.execute(create_table_item)

#cursor.execute("INSERT INTO items VALUES('test',10.99)")
con.commit()
con.close()
