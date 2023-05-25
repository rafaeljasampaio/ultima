import sqlite3

conexao = sqlite3.connect('tarefas.db')

cursor =  conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS categorias (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL UNIQUE
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    data TEXT,
    status INTEGER CHECK (status IN (0,1)),
    id_categoria INTEGER,
    FOREING KEY (id_categoria) REFERENCES categorias (id)
);
''')