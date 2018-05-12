import sqlite3

conn=sqlite3.connect('database.db')
cursor=conn.cursor()

#cursor.execute('Create table users (login text, password text, email text,\
#                first_name text, last_name text)')

cursor.execute('Insert into users values ("empeko","emp123","emp@ya.ru","Viktor","Mun")')
result=cursor.execute('Select * from users where login="empeko"')

print(result.fetchall())

conn.commit()
conn.close()
