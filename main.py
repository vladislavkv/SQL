import sqlite3

conn=sqlite3.connect('database.db')
cursor=conn.cursor()

#cursor.execute('Create table users (login text, password text, email text,\
#                first_name text, last_name text)')

#cursor.execute('Insert into users values ("empeko","emp123","emp@ya.ru","Viktor","Mun")')
#result=cursor.execute('Select * from users')

#print(result.fetchall())

while True:
    a=int(input('Enter "1" for Sign in, "2" for Sign up: '))

    if a==1:
        login=input('Login: ')
        password=input('Password: ')
        result=cursor.execute('Select * from users where login="%s" and password="%s"'%(login,password)).fetchone()
        if result is not None:
            print('Welcome!')
        else:
            print('Incorrect login or password!')
    elif a==2:
        login=input('Придумайте логин: ')
        password=input('Придумайте пароль: ')
        email=input('Введите email: ')
        first_name=input('Введите Ваше имя: ')
        last_name=input('Введите Вашу фамилию: ')
        cursor.execute('Insert into users values ("%s","%s","%s","%s","%s")'%(login,password,email,first_name,last_name))

    conn.commit()
    conn.close()
