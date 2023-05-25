import sqlite3

conexao = sqlite3.connect('bdevento.sqlite3')
cursor = conexao.cursor()

descricao = input('Digite a Descrição do Evento: ')
data = input('Digite a Data do Evento: ')


sql = 'SELECT id, descricao FROM categoria'
categorias = cursor.execute(sql)
print('Categorias disponíveis: ')
for categoria in categorias:
    print('ID:', categoria[0], 'Descrição:',  categoria[1])

categoria_id = int(input('Digite o ID da Cetegoria desejada: '))

sql = 'INSERT INTO evento (descricao, data, categoria_id) VALUES (?, ?, ?)'

valores = [descricao, data, categoria_id]

cursor.execute(sql, valores)

conexao.commit()
conexao.close()

print('\n','Evento incluído com sucesso!')


