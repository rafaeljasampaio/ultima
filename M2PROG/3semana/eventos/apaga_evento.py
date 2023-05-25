import sqlite3

conexao = sqlite3.connect('bdevento.sqlite3')
cursor = conexao.cursor()

sql = 'SELECT id, descricao, data FROM evento'

eventos = cursor.execute(sql)
print('Eventos disponiveis: ')
for evento in eventos:
    print('ID:', evento[0], 'Descrição:',  evento[1], 'Data:', evento[2])

apagar_evento = input('Digite a ID do evento que deseja apagar: ')

sql = 'DELETE FROM evento WHERE id = ?'

cursor.execute(sql,apagar_evento)

conexao.commit()
conexao.close()

print('\n'
     'Evento Apagado com sucesso!')
