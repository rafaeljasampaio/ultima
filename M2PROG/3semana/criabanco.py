import sqlite3

conexao = sqlite3.connect('bdeventos.sqlite3')
cursor = conexao.cursor()

sql = '''
    CREATE TABLE categoria (
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao_categoria text(100)
);
'''

sql2 = '''
    CREATE TABLE evento (
        id_evento INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao_evento TEXT(150),
        categoria_id INTEGER,
        "data" TEXT(10),
        CONSTRAINT evento_FK FOREIGN KEY (categoria_id) 
        REFERENCES categoria(id_categoria) ON DELETE CASCADE
);
'''

cursor.execute(sql)

cursor.execute(sql2)

conexao.commit()
conexao.close()
