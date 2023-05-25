import sqlite3

conexao = sqlite3.connect('bdeventos.sqlite3')
cursor = conexao.cursor()


while True:
    evento = input('Digite o nome do evento ou -1 para sair ')
    categoria = int(input('Digite o nome do categoria ou -1 para sair '))
    data = input('Digite o nome do evento ou -1 para sair DD/MM/AAAA ')
    
    
    if evento == '-1' or data == '-1' or categoria == '-1':
        break
    
    p1 = ("INSERT INTO evento (descricao_evento, categoria_id, data) VALUES ('")
    p2 = ("');")
    sql = ({p1} + {evento} , +{categoria}, +{data} +{p2})

    cursor.execute(sql)
d    
conexao.commit()
conexao.close()
