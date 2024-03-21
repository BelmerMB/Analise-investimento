'''
Description: all functions to manipulate a Relational database with 'sqlite3'
'''

import sqlite3
from sqlite3 import Error

#-------Table Connection------
def connect_db(path_db):
    connection = None
    try:
        connection=sqlite3.connect(path_db)
    except Error as error:
        print(error)
    return connection

#-------Table CREATE-------
def create_db(connection, command):
    try:
        cursor = connection.cursor()
        cursor.execute(command)
        print(f'Tabela criada') 
    except Error as er:
        print(er)

#-------Table UPDATE-------
        
#-------Table INSERT-------
        
#-------Table DELET-------
        
#-------Table SELECT-------

#-------comandos de teste ----------
vcon = connect_db('./apoostas.db')


