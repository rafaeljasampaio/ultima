import sqlite3

conexao = sqlite3.connect('bdevento.sqlite3')
cursor = conexao.cursor()

while True:
    
    descricao = input("Digite a descrição da categoria: (-1 para sair) ")
    if descricao == '-1':
        break
    sql = 'INSERT INTO categoria (descricao) VALUES (?)'
    valores = [descricao]
    cursor.execute(sql, valores)

conexao.commit()
conexao.close()
