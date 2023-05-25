import sqlite3

conexao = sqlite3.connect('bdevento.sqlite3')
cursor = conexao.cursor()

sql = '''
        SELECT i.id, i.nome , p.descricao as "Evento", p."data" 
        FROM evento as p, inscricao  as i
        WHERE  p.id = i.evento_id order by p.descricao
'''

consulta_eventos = cursor.execute(sql)

for evento in consulta_eventos:
    print('ID', evento[0], 'Descrição', evento[1], 'Data', evento[2], 'Descrição categoria', evento[3])


conexao.commit()
conexao.close()
