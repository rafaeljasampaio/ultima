import sqlite3  

conexao = sqlite3.connect('bd.sqlite3')

cursor = conexao.cursor()

sql = '''
    INSERT INTO tarefa(nome_tarefa, data, status, id_categoria) VALUES ("MODELAGEM CAMISA","2023.04.21","Em Andamento",2)
'''

cursor.execute(sql)

conexao.commit()
conexao.close()
