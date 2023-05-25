import sqlite3

conexao = sqlite3.connect('bdeventos.sqlite3')
cursor = conexao.cursor()


while True:
    nome = input('Digite o nome da categoria: digite -1 para sair')

    if nome == '-1':
        break
    
    p1 = ("INSERT INTO categoria (descricao_categoria) VALUES ('")
    p2 = ("')")
    sql = (p1 + nome + p2)
    cursor.execute(sql)
    
conexao.commit()
conexao.close()
