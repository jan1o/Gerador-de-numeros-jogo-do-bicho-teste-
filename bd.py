import sqlite3

class bd:

    def create_table():
        connection = sqlite3.connect('bichos.db')
        c = connection.cursor()
        c.execute('CREATE TABLE bichos (id integer, peso integer)')
        connection.commit()
        
    def inserts():
        connection = sqlite3.connect('bichos.db')
        c = connection.cursor()
        c.execute("INSERT INTO bichos VALUES(1, 1)")
        c.execute("INSERT INTO bichos VALUES(2, 1)")
        c.execute("INSERT INTO bichos VALUES(3, 1)")
        c.execute("INSERT INTO bichos VALUES(4, 1)")
        c.execute("INSERT INTO bichos VALUES(5, 1)")
        c.execute("INSERT INTO bichos VALUES(6, 1)")
        c.execute("INSERT INTO bichos VALUES(7, 1)")
        c.execute("INSERT INTO bichos VALUES(8, 1)")
        c.execute("INSERT INTO bichos VALUES(9, 1)")
        c.execute("INSERT INTO bichos VALUES(10, 1)")
        c.execute("INSERT INTO bichos VALUES(11, 1)")
        c.execute("INSERT INTO bichos VALUES(12, 1)")
        c.execute("INSERT INTO bichos VALUES(13, 1)")
        c.execute("INSERT INTO bichos VALUES(14, 1)")
        c.execute("INSERT INTO bichos VALUES(15, 1)")
        c.execute("INSERT INTO bichos VALUES(16, 1)")
        c.execute("INSERT INTO bichos VALUES(17, 1)")
        c.execute("INSERT INTO bichos VALUES(18, 1)")
        c.execute("INSERT INTO bichos VALUES(19, 1)")
        c.execute("INSERT INTO bichos VALUES(20, 1)")
        c.execute("INSERT INTO bichos VALUES(21, 1)")
        c.execute("INSERT INTO bichos VALUES(22, 1)")
        c.execute("INSERT INTO bichos VALUES(23, 1)")
        c.execute("INSERT INTO bichos VALUES(24, 1)")
        c.execute("INSERT INTO bichos VALUES(25, 1)")
        connection.commit()

    def addPeso(bicho, peso):
        connection = sqlite3.connect('bichos.db')
        c = connection.cursor()
        c.execute("UPDATE bichos SET peso = peso + ? WHERE id = ?",(peso, bicho))
        connection.commit()

    def getBichos():
        connection = sqlite3.connect('bichos.db')
        c = connection.cursor()
        c.execute("SELECT * from bichos ORDER BY peso DESC")
        
        lista = []
        for b in c.fetchall():
            lista.append(b)
        return lista





        







