import sqlite3

conn=sqlite3.connect('database.db')
cursor=conn.cursor()

#cursor.execute('Create table users (login text, password text, email text,\
#                first_name text, last_name text)')

#cursor.execute('Insert into users values ("empeko","emp123","emp@ya.ru","Viktor","Mun")')
#result=cursor.execute('Select * from users')

#print(result.fetchall())

print('Enter "1" for Sign in, "2" for Sign up')
a=int(input())

if a==1:
    login=input('Login: ')
    password=input('Password: ')
    result=cursor.execute('Select * from users where login="%s" and password="%s"'%(login,password)).fetchone()
    if result is not None:
        print('Welcome!')
    else:
        print('Incorrect login or password!')

conn.commit()
conn.close()
