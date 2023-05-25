import sqlite3

conexao = sqlite3.connect('bdevento.sqlite3')
cursor = conexao.cursor()

sql = 'SELECT id, descricao, data FROM evento'

eventos = cursor.execute(sql)
print('Eventos disponiveis: ')
for evento in eventos:
    print('ID:', evento[0], 'Descrição:',  evento[1], 'Data:', evento[2])

evento_id = input('Digite o ID do evento desejado: ')
nome = input('Digite seu nome: ')
email = input('Digite seu e-mail: ')


sql = 'INSERT INTO inscricao (nome, email, evento_id) VALUES (?, ?, ?)'

valores = [nome, email, evento_id]

cursor.execute(sql, valores)

conexao.commit()
conexao.close()

print('\n'
     'Inscrição Concluída com sucesso!')