import sqlite3

conexao = sqlite3.connect('bdevento.sqlite3')
cursor = conexao.cursor()

sql = 'SELECT id, descricao, data FROM evento'

eventos = cursor.execute(sql)
print('Eventos disponiveis: ')
for evento in eventos:
    print('ID:', evento[0], 'Descrição:',  evento[1], 'Data:', evento[2])

evento_consulta = int(input('Digite o evento que gostaria de consultar os participantes: '))

sql = 'SELECT id, nome, email, evento_id FROM inscricao'

participantes = cursor.execute(sql)

print('Participantes do evento são: ')

for participante in participantes:
    if evento_consulta == participante[3]:
        print('Id:', participante[0], 'Nome:', participante[1], 'e-mail:', participante[2])


conexao.commit()
conexao.close()








