import sqlite3

conexao = sqlite3.connect('dbeventos.sqlite3')

cursor = conexao.cursor()

sql = '''
select titulo_evento 
	  ,id_organizadores
	  ,eventos.data_evento 
	  ,organizador.nome 
from eventos
inner join organizador_evento on eventos.id_evento == organizador_evento.id_eventos
inner join organizador on organizador.id_organizador == organizador_evento.id_organizadores 
'''

print(cursor.execute(sql))

conexao.commit()
conexao.close()

