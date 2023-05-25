import sqlite3

conexao = sqlite3.connect('bdevento.sqlite3')
cursor = conexao.cursor()

sql = '''
    SELECT id, descricao, categoria_id, data FROM evento
'''

eventos = cursor.execute(sql)

print("Eventos disponiveis")
for evento in eventos:
    print("ID:", evento[0], "Descrição:", evento[1], "Categoria ID:", evento[2], "Data:", evento[3])

evento_id = input("Digite o ID do Evento que Deseja atualizar: ")

descricao = input("Digite a nova descrição: ")
data = input("Digite a nova Data: ")

sql = 'UPDATE evento SET descricao = ?, data = ? WHERE id = ?'

valores = [descricao, data, evento_id]
cursor.execute(sql, valores)
conexao.commit()
conexao.close()

print("Alterado com sucesso")
