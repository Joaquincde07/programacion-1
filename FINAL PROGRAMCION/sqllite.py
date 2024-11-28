import sqlite3


conexion = sqlite3.connect('final.db')


cursor = conexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT,
                    edad INTEGER)''')


cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("Juan", 25))
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", ("lucas", 23))


conexion.commit()

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)

conexion.close()
