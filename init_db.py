import sqlite3

con = sqlite3.connect('sync_guancha.db')
cur = con.cursor()

cur.execute('''CREATE TABLE sync (id text, title text, href text, status int, time timestamp)''')
con.commit()
con.close()